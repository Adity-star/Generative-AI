from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load all environment variables from .env
load_dotenv()

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load geminipro
def get_geminipro(input_prompt: str, image: Image.Image, prompt: str) -> str:
   
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Generate content based on input, image, and prompt
    response = model.generate_content([input_prompt, image, prompt])
    
    print("Response:", response)
    print("Response Type:", type(response))


    if isinstance(response, dict):
        return response.get('text', 'No text found')

    elif hasattr(response, 'text'):
        return response.text
    else:
        raise ValueError("Unexpected response structure.")
    

# Function to prepare image for input
def input_img_setup(upload_file) -> Image.Image:
    if upload_file is not None:

        # Read the file as a PIL Image
        image = Image.open(upload_file)
        return image
    else:
        raise FileExistsError("No file uploaded. Please upload the file")
    

# Build frontend interface
st.set_page_config(page_title="Invoice Extractor")

st.header('Gemini Pro application')

input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = input_img_setup(uploaded_file)  
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the invoice")

if submit:
    if uploaded_file is None:
        st.warning("Please upload an image to extract invoice information.")
    else:
        response = get_geminipro(input_prompt, image, input_prompt)

        st.subheader("The response is:")
        st.write(response)