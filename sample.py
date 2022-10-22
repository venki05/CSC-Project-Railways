#Importing streamlit and functions
from typing import Container
import streamlit as st
import login

# Styling the page
st.set_page_config(
    page_title="Retro",
    page_icon="🧊",
    layout="wide"
)
page_image="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1442570468985-f63ed5de9086?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fHRyYWlufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60");
    background-size: cover;
    background-repeat: no-repeat;
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
with st.container():
    st.header("Welcome to Retro!")
    button1=st.button("Sign up")
    button2=st.button("Log in")
    if button1:
        login.signup()
    elif button2:
        login.login()


    
