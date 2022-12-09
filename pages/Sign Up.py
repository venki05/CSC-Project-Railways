# importing libraries
import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
#css
page_image="""
<style>
[data-testid="stAppViewContainer"]{

    background-image: linear-gradient(-225deg, #FFFEFF 0%, #D7FFFE 100%);
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
                    @import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@1,900&display=swap');
                    html, body, [class*="css"]{
                        font-family: 'Raleway', sans-serif;
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
    with st.form("form1"):
        name = st.text_input("name")
        username = st.text_input("username")
        mailid = st.text_input("mail id")
        check = 0
        for i in ('@gmail.com','@outlook.com','@yahoo.com','@yandex.com','@icloud.com'):
            if i in mailid:
                check = 1
        if mailid !='':
            if check != 1:
                st.warning('Invalid Email ID')

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
