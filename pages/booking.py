#Import
import streamlit as st
import pandas as pd
from deta import Deta
st.set_page_config(initial_sidebar_state="collapsed")
#st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
#CSS
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


#Train Data in Deta
DataKey_Trains = 'd05gnskf_K83euLqNybw5SDKVvEMgxYTBs4y7n966'
deta_Trains = Deta(DataKey_Trains)
db_trains = deta_Trains.Base("TrainsDB")

def fetch_all_trains():
    res_trains = db_trains.fetch()
    return res_trains.items   


# Dashboard Function
def user_dashboard():
    #Dashboard of User
    col1,col2,col3=st.columns(3)
    with col1:
        st.write("Go ahead and book tickets for your amazing journey")
        book_button = st.button("Book Tickets")
        if book_button:
            st.markdown('''<head>
            <title>HTML Redirect</title>
            <meta http-equiv="refresh" content="0.5; url =
            http://localhost:8501/trainselection" />
            </head>''',unsafe_allow_html=True)
        logout_button=st.button("Logout")
        st.write("Want to cancel the tickets you booked earlier?")
        cancel_button = st.button("Cancel Tickets")
        if logout_button:
            st.markdown('''<head>
                    <title>HTML Redirect</title>
                    <meta http-equiv="refresh" content="0.5; url =
                    http://localhost:8501/Login" />
                    </head>''',unsafe_allow_html=True)
        if cancel_button:
            st.markdown('''<head>
                    <title>HTML Redirect</title>
                    <meta http-equiv="refresh" content="0.5; url =
                    http://localhost:8501/Cancel" />
                    </head>''',unsafe_allow_html=True)
    with col2:
        pass
    with col3:
        st.image('login.jpg',width=300)

user_dashboard()


