# Import
from deta import Deta
import streamlit as st
import streamlit_authenticator as stauth
st.set_page_config(initial_sidebar_state="collapsed")
#st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

# CSS
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


# Login
def login():
    menu=['Admin','User']
    st.markdown("<h1 class='big-font'>Login</h1>", unsafe_allow_html=True)
    choice=st.selectbox("Please Select...",menu)
    if choice=='User':
        global flag
        flag=1
        username=st.text_input("username:")
        password=st.text_input("password: ",type="password")
        users = fetch_all_users()
        for i in users:
            c=0
            if username=='' or password=='':
                c=1
            elif i["username"]==username and i["pwd"]==password:
                st.success("Logged in as {}".format(username))
                c=1
                return True
        if c==0:
                st.error("Login credenials are wrong")
    else:
        flag=2
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='' or password=='':
            pass
        elif username=='admin' and password=='indianrailway':
            st.success("Logged in as Admin")
            return True
        else :
            st.error("Login credenials are wrong")
            return False
col1,col2,col3=st.columns(3)
with col1:
    flag=0
    s=login()
with col2:
    pass
with col3:
    st.image('login.jpg',width=400)
if s:
    if flag==1:
        st.markdown('''<head>
        <title>HTML Redirect</title>
        <meta http-equiv="refresh" content="2; url =
        http://localhost:8501/booking" />
        </head>''',unsafe_allow_html=True)

    if flag==2:
        st.markdown('''<head>
        <title>HTML Redirect</title>
        <meta http-equiv="refresh" content="2; url =
        http://localhost:8501/Admin" />
    </head>''',unsafe_allow_html=True)

    