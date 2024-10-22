import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemeni pro vision model and get response

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemeni_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

##initialize streamlit app

st.set_page_config(page_title="Image Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpeg","jpg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Upload Image.", use_column_width=True)

submit=st.button("Tell me about the image")

##if submit is clicked 
if submit:
    response = get_gemeni_response(input,image)
    st.subheader("The Response is")
    st.write(response)