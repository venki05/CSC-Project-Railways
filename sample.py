import streamlit as st
import login
st.set_page_config(
    page_title="Retro",
    page_icon="🧊",
    layout="wide"
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

login.login()
    
