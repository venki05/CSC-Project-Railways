# importing libraries
from turtle import onclick
import streamlit as st


def login():
    menu=['Admin','User']
    choice=st.selectbox("Please select...",menu)
    if choice=='User':
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='' or password=='':
            pass
        elif username=='railway' and password=='irctc':
            st.success("Logged in as {}".format(username))
        else:
            st.error("Login credenials are wrong")
    else:
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='' or password=='':
            pass
        elif username=='admin' and password=='indianrailway':
            st.success("Logged in as Admin")
        else :
            st.error("Login credenials are wrong")

def form():
    st.markdown("<h1 style='text-align:center'>Sign Up</h1>", unsafe_allow_html=True)
    with st.form("form2"):
        
        col1,col2 = st.columns(2)
        firstname = col1.text_input("first name")
        lastname = col2.text_input("last name")
        mailid = st.text_input("email address")
        pwd = st.text_input("password")
        cpwd = st.text_input("confirm password")
        submit = st.form_submit_button(label="submit",on_click=login)
        if submit:
            c=0
            for i in (firstname,lastname,mailid,pwd,cpwd):
                if i == "":
                    st.warning("please fill the above fields")
                    c=1
                    break
            if pwd!=cpwd:
                st.warning("passwords are not matching")
            else:
                if c==0:
                    st.success("Signed up")
                
form()
