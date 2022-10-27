import email
import streamlit as st

with st.form("my_form"):
   st.write("Please fill the details to sign up.")
   name=st.text_input("Enter your name.")
   email=st.text_input("Enter your email id.")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.success("Successfully signed in")

st.write("Outside the form")