import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io

# Title and description
st.set_page_config(page_title="Ludy 1.1 – Image Generator", layout="wide")

st.title("🖼️ Ludy 1.1 – Ready-to-Use AI Image Generator")
st.markdown("""
Welcome to **Ludy 1.1**!  
This app uses a pre-trained Stable Diffusion 1.5 model to generate images from your text prompts.  
No training, no keys, no complicated setup — just type and create!

**How to use:**
- Write any prompt (English works best)
- Click **Generate Image**
- Wait 30–90 seconds (first time is slower while model downloads)
- Enjoy the result!

**Examples:**
- "a cartoon cactus sitting on the toilet with a microphone reaching out to a crowd, funny style"
- "red sports car driving at sunset with mountains, cinematic lighting"
- "cute fluffy cat astronaut floating in space eating pizza, kawaii style"
""")

# Load the pre-trained model (downloads ~4 GB first time, then cached)
@st.cache_resource
def load_model():
    st.info("Loading model for the first time... This may take a few minutes.")
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        safety_checker=None,  # Disable NSFW filter for creative/funny prompts
    )
    pipe = pipe.to("cpu")  # Streamlit Cloud has no GPU
    pipe.enable_attention_slicing()  # Reduces memory usage on CPU
    return pipe

pipe = load_model()

# Prompt input
prompt = st.text_input("Enter your prompt:", 
                       "cartoonish cactus sitting on the toilet with a microphone reaching out to a crowd, funny style")

# Generate button
if st.button("Generate Image"):
    if prompt.strip():
        with st.spinner("Generating image... (30–90 seconds on CPU)"):
            try:
                # Generate the image
                image = pipe(
                    prompt,
                    num_inference_steps=50,
                    guidance_scale=7.5,
                    height=512,
                    width=512
                ).images[0]

                # Display the image
                st.image(image, caption=f"Generated: {prompt}")

                # Download button
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download Image",
                    data=byte_im,
                    file_name="ludy_generated.png",
                    mime="image/png"
                )

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}\nTry a simpler prompt or wait a bit.")
    else:
        st.warning("Please enter a prompt!")

st.markdown("---")
st.caption("Powered by Stable Diffusion 1.5 • Running on Streamlit Cloud • Created by Bogdan")
