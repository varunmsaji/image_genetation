import streamlit as st 
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#function to generate a image using dalle

import openai

def generate_image_openai(input_text):
    response = openai.Image.create(
        prompt=input_text,
        n=1,
        size="512x512",
        # Add your OpenAI API key here
        api_key="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"
    )

    # Access the generated image URL from the response
    image_url = response["data"][0]["url"]
    return image_url



choice = st.sidebar.selectbox("select your choice",["home","DAll-e","diffusers"])


if choice =='home':
    st.title("ai image generation app")
    with st.expander("about the app"):
        st.write("this is app to generate images from text using open ai dall e")

elif choice =='DAll-e':
    st.title("image generation using dalle")
    input_text = st.text_input("enter the input")
    if input_text is not None:
        if st.button("generate image"):
            st.info(input_text)
            image_url = generate_image_openai(input_text)
            st.image(image_url)

elif choice=='diffusers':
    st.title("image genereation using diffussers")