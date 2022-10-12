import streamlit as st
import random
st.title("Login")
r=random.randint(100000,900000)
def login():
    menu=['Admin','User']
    choice=st.selectbox("Please select...",menu)
    if choice=='User':
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='railway' and password=='irctc':
            st.success("Logged in as user"+str(r))
        elif username!='railway' and password!='irctc':
            st.write("Login credenials are wrong")
    else:
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='admin' and password=='indianrailway':
            st.success("Logged in as Admin")
        elif username!='admin' and password!='indianrailway' :
            st.write("Login credenials are wrong")

login()
    
