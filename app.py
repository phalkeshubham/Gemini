from dotenv import load_dotenv
load_dotenv() ##loading all the envoirment variables

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemeni pro model and get response

model=genai.GenerativeModel("gemini-pro")
def get_gemeni_response(question):
    response=model.generate_content(question)
    return response.text

## initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

##When submit is clicked

if submit:
    response=get_gemeni_response(input)
    st.write(response)
