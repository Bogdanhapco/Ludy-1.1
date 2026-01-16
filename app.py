import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from PIL import Image
import io
import math

# Hyperparameters for 128x128 res
device = torch.device("cpu")  # Streamlit Cloud uses CPU
timesteps = 500
image_size = 128
channels = 3
betas = torch.linspace(0.0001, 0.02, timesteps).to(device)
alphas = 1.0 - betas
alphas_cumprod = torch.cumprod(alphas, dim=0)
alphas_cumprod_prev = F.pad(alphas_cumprod[:-1], (1, 0), value=1.0)
sqrt_recip_alphas = torch.sqrt(1.0 / alphas)
sqrt_alphas_cumprod = torch.sqrt(alphas_cumprod)
sqrt_one_minus_alphas_cumprod = torch.sqrt(1.0 - alphas_cumprod)
posterior_variance = betas * (1.0 - alphas_cumprod_prev) / (1.0 - alphas_cumprod)

# Simple U-Net for 128x128
class SimpleUNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.down1 = nn.Sequential(nn.Conv2d(3, 64, 3, padding=1), nn.ReLU(), nn.Conv2d(64, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))
        self.down2 = nn.Sequential(nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(), nn.Conv2d(128, 128, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))
        self.down3 = nn.Sequential(nn.Conv2d(128, 256, 3, padding=1), nn.ReLU(), nn.Conv2d(256, 256, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))
        self.bottleneck = nn.Sequential(nn.Conv2d(256, 512, 3, padding=1), nn.ReLU(), nn.Conv2d(512, 512, 3, padding=1), nn.ReLU())
        self.up3 = nn.Sequential(nn.ConvTranspose2d(512, 256, 2, stride=2), nn.Conv2d(512, 256, 3, padding=1), nn.ReLU())
        self.up2 = nn.Sequential(nn.ConvTranspose2d(256, 128, 2, stride=2), nn.Conv2d(256, 128, 3, padding=1), nn.ReLU())
        self.up1 = nn.Sequential(nn.ConvTranspose2d(128, 64, 2, stride=2), nn.Conv2d(128, 64, 3, padding=1), nn.ReLU())
        self.out = nn.Conv2d(64, 3, 1)

    def forward(self, x, t):
        # Basic time embedding
        t_emb = torch.sin(t.unsqueeze(-1) * 0.02).expand(-1, x.size(1), x.size(2), x.size(3))
        x = x + t_emb
        
        d1 = self.down1(x)
        d2 = self.down2(d1)
        d3 = self.down3(d2)
        b = self.bottleneck(d3)
        u3 = self.up3(b)
        u3 = torch.cat([u3, d3], dim=1)
        u2 = self.up2(u3)
        u2 = torch.cat([u2, d2], dim=1)
        u1 = self.up1(u2)
        u1 = torch.cat([u1, d1], dim=1)
        return self.out(u1)

# Load model (from-scratch, no pre-trained)
@st.cache_resource
def load_model():
    model = SimpleUNet().to(device)
    # Here you can load trained weights if you train locally: model.load_state_dict(torch.load('my_model.pth'))
    return model

model = load_model()

# Generate function
@torch.no_grad()
def generate_image():
    x = torch.randn(1, channels, image_size, image_size).to(device)
    for t in reversed(range(timesteps)):
        t_tensor = torch.full((1,), t, dtype=torch.long).to(device)
        predicted_noise = model(x, t_tensor)
        alpha = alphas[t]
        alpha_cumprod = alphas_cumprod[t]
        beta = betas[t]
        if t > 0:
            noise = torch.randn_like(x)
        else:
            noise = torch.zeros_like(x)
        x = 1 / torch.sqrt(alpha) * (x - ((1 - alpha) / torch.sqrt(1 - alpha_cumprod)) * predicted_noise) + torch.sqrt(beta) * noise
    x = (x.clamp(-1, 1) + 1) / 2
    x = (x * 255).byte().cpu().permute(0, 2, 3, 1).numpy()[0]
    return Image.fromarray(x)

# --- Streamlit App for Ludy 1.1 ---
st.set_page_config(page_title="Ludy 1.1 – Image Generator", layout="wide")

st.title("🖼️ Ludy 1.1 – AI Diffusion Image Generator")
st.markdown("""
This is a separate app for generating images using our own from-scratch diffusion model at 128x128 resolution.  
It's basic (abstract/noise-like results) since it's not pre-trained — you can train it locally on your GPU for better results.  
Type a prompt and click Generate!  

Example prompts: "red car", "sunset landscape", "cartoon cactus"
""")

# Input
prompt = st.text_input("Enter your prompt:")
generate_button = st.button("Generate Image")

if generate_button:
    if prompt:
        with st.spinner("Generating 128x128 image (may take 1–2 minutes on CPU)..."):
            img = generate_image()
        st.image(img, caption=f"Generated for '{prompt}'")
        st.download_button("Download Image", img.tobytes(), "ludy_image.png", "image/png")
    else:
        st.error("Please enter a prompt!")

st.markdown("""
Note: For better quality, train the model locally on your GPU and upload weights to this repo. And we in the next update will train Ludy ou our Datacenter so you dont have to
""")
