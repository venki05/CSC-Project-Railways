#Importing streamlit and functions
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
    background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5oy1S4KvO2j-KqSSBJBdc6G4Rn9u8IgeKOw&usqp=CAU");
    background-size: cover;
}

[data-testid="stHeader"]{
    background-color: rgba(0,0,0,1);
}

[data-testid="stVerticalBlock"]{
    
}
</style>
"""

st.markdown(page_image,unsafe_allow_html=True)

# Font
streamlit_style = """
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Monoton&display=swap');
                    html, body, [class*="css"]{
                        font-family: 'Monoton', cursive;
                    }
                    </style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

# Font Size
st.markdown("""
<style>
.big-font {
    font-size:75px !important;
    color: black
}

.medium-font {
    font-size:50px !important;
    color: black
}

.small-font{
    font-size:25px !important;
    color: black
}
</style>
""", unsafe_allow_html=True)

#column 1
content,logo= st.columns(2)

with content:
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to Retro!</h1>", unsafe_allow_html=True)

with logo:
    st.image("Retro-logos_black.png")

# column 2
col1 , col2 = st.columns(2)

with col1:
    st.image("Mobile login.png")

with col2:
    st.markdown("<p class='small-font'>Here at Retro, you are provided a simple interface for train ticket reservation.</p></h2>", unsafe_allow_html=True)
    st.markdown("<p class='small-font'>Please log in to reserve your tickets.</p></h2>", unsafe_allow_html=True)
    st.markdown("<p class='small-font'>Please log in to reserve your tickets.</p></h2>", unsafe_allow_html=True)
    st.markdown("<a href='http://localhost:8501/Login'>login</h2>", unsafe_allow_html=True)


    
