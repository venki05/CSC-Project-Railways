# importing libraries
import streamlit as st

# Functions for deta
from deta import Deta

DataKey = 'd05gnskf_zBRSkEhbeCFKcaKFwZHLopyWodKwN32b'

deta = Deta(DataKey)

db = deta.Base("loginDB")

def insert_user(name,username,mailid,password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"name":name, "username": username,"mailid":mailid,"pwd": password})

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items


def get_user(username):
    """If not found, the function will return None"""
    return db.get(username)


def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)


def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)



def form():
    st.markdown("<h1 style='text-align:center'>Sign Up</h1>", unsafe_allow_html=True)
    with st.form("form2"):
        name = st.text_input("name")
        username = st.text_input("username")
        mailid = st.text_input("mail id")
        pwd = st.text_input("password")
        cpwd = st.text_input("confirm password")
        submit = st.form_submit_button(label="submit")
        if submit:
            c=0
            for i in (name,username,mailid,pwd,cpwd):
                if i == "":
                    st.warning("please fill the above fields")
                    c=1
                    break
            if pwd!=cpwd:
                st.warning("passwords are not matching")
            else:
                if c==0:
                    st.success("Signed up")
                    insert_user(name,username,mailid,pwd)
                    st.markdown("<p class='small-font'>Click here to <a href='http://localhost:8501/Login'>log in</a> to reserve your tickets.</p></h2>", unsafe_allow_html=True)
                
form()
