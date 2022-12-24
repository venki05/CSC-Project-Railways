#Imports
import streamlit as st
from deta import Deta
import pandas as pd
st.set_page_config(initial_sidebar_state="collapsed")
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
                    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap');
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
    font-size:65px !important;
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


#Passenger
Datakey_passengers = 'd05gnskf_AMQg96QfvUkNB1SBq9ExVWRnLCg5KM8J'
deta_passengers = Deta(Datakey_passengers)
db_passengers = deta_passengers.Base("passengersDB")

st.header("Cancellation of Tickets")

#Functions
def delete_passenger(key):
    """Always returns None, even if the key does not exist"""
    return db_passengers.delete(key)

def fetch_all_passengers():
    res_passengers = db_passengers.fetch()
    return res_passengers.items

def load_data():
    return pd.DataFrame(passengers)

#Algo 

passengers = fetch_all_passengers()
df = load_data()
cancel = st.text_input("Enter your name and trainname in the format name//trainname")
delete= st.button("Delete")
keyname = df[['cancel','key']]
for i in range(len(keyname)):
    if cancel == keyname['cancel'][i]:
        key = keyname['key'][i]
        if delete:
            delete_passenger(key)
            st.success("Cancellation was successful.")
            st.markdown('''<head>
                            <title>HTML Redirect</title>
                            <meta http-equiv="refresh" content="1; url =
                            http://localhost:8501/booking" />
                        </head>''',unsafe_allow_html=True)