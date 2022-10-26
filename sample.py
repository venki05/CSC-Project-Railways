#Importing streamlit and functions
from turtle import width
from typing import Container
import streamlit as st
import login
from PIL import Image

# Styling the page
st.set_page_config(
    page_title="Retro",
    page_icon="abc",
    layout="wide"
)
page_image="""
<style>
[data-testid="stAppViewContainer"]{
    background-color:black;
}

[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}

[data-testid="stVerticalBlock"]{
    
}
</style>
"""


st.markdown(page_image,unsafe_allow_html=True)

#Content and main program
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("Retro-logos_white.png")

with col3:
    st.write(' ')

    
with st.container():
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to Retro!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'><p>Here at Retro, you are provided a simple interface for train ticket reservation.</p></h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'><p>Please log in to reserve your tickets.</p></h3>", unsafe_allow_html=True)
    button2=st.button("login")
    st.markdown("<h3 style='text-align: center; color: white;'><p>Dont have an account? Then go ahead and create one</p></h3>", unsafe_allow_html=True)
    button1=st.button("Sign up")
    if button1:
        login.signup()
    elif button2:
        login.login()


    
