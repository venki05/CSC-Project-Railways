import streamlit as st

menu=['Admin','User']
choice=st.selectbox("Please select...",menu)
if choice=='User':
    username=st.text_input("user id: ")
    password=st.text_input("password: ",type="password")
    if username=='' or password=='':
        pass
    elif username=='railway' and password=='irctc':
        st.success("Logged in as user"+str(r))
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
        