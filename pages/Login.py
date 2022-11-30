# Import
from deta import Deta
import streamlit as st
import streamlit_authenticator as stauth
# CSS
with open('style.css') as file:
    st.markdown("<style>file.read()</style>",unsafe_allow_html = True)

# Deta Connection and Functions
DataKey = 'd05gnskf_zBRSkEhbeCFKcaKFwZHLopyWodKwN32b'

deta = Deta(DataKey)

db = deta.Base("loginDB")


def insert_user(name,mailid,password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"name":name, "username": username,"pwd": password})

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

# Data



# Login
def login():
    menu=['Admin','User']
    choice=st.selectbox("Please select...",menu)
    if choice=='User':
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        users = get_user(username)
        if users["username"]==username and users["pwd"]==password:
            st.success("Logged in as {}".format(username))
            return True
        else:
            st.error("Login credenials are wrong")
            return False

        '''
        if username=='' or password=='':
            pass
        elif username=='railway' and password=='irctc':
            st.success("Logged in as {}".format(username))
            return True
        else:
            st.error("Login credenials are wrong")
            return False
        '''
    else:
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='' or password=='':
            pass
        elif username=='admin' and password=='indianrailway':
            st.success("Logged in as Admin")
        else :
            st.error("Login credenials are wrong")

s=login()
if s:
    st.markdown('''<head>
    <title>HTML Redirect</title>
    <meta http-equiv="refresh" content="2; url =
    http://localhost:8501/booking" />
</head>''',unsafe_allow_html=True)
    