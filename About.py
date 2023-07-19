import streamlit as st
from PIL import Image


st.title('About System')


st.markdown("Scaling other language-related jobs is accomplished through the use of natural language processing, which enables computers to speak with people in their own language. As an illustration, NLP enables computers to read text, hear voice, understand it, gauge sentiment, and identify the key points.")

image = Image.open ( 'sentiment_analysis_1.png' )
st.image ( image )

st.write(" * Firstly this system tries to get the inputs of the desired product/description.")
st.write(" * Then using the model it predicts the product type or the sentiment of the corresponding review/description.")
st.write(" * Also, add-on to this it tries to visualize the insights after selecting the parameters.")