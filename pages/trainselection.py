#Imports
import streamlit as st
from deta import Deta
import pandas as pd
st.set_page_config(initial_sidebar_state="collapsed")
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

# DB connection
#Trains

DataKey_Trains = 'd05gnskf_K83euLqNybw5SDKVvEMgxYTBs4y7n966'
deta_Trains = Deta(DataKey_Trains)
db_trains = deta_Trains.Base("TrainsDB")

#Passenger
Datakey_passengers = 'd05gnskf_AMQg96QfvUkNB1SBq9ExVWRnLCg5KM8J'
deta_passengers = Deta(Datakey_passengers)
db_passengers = deta_passengers.Base("passengersDB")

#Function
def fetch_all_trains():
    res_trains = db_trains.fetch()
    return res_trains.items   

trains = fetch_all_trains()# Fetchin trains

flag = 0
#Form
c=0
a,b,c,d,e = '', '', '', '', ''
with st.form("places"):
    From = st.text_input("From")
    To = st.text_input("To")
    submit = st.form_submit_button("submit")

with st.form("passenger"):
    l=['please select...']
    for i in trains:
        s=(i['To'],i['Stop 1'],i['Stop 2'],i['Stop 3'],i['Stop 4'],i['Stop 5'],i['From'])
        if From in s and To in s:
            df = pd.DataFrame(i,index=[""])
            l.append(i['Train Name'])
            st.write(df[['Train Name','To','Stop 1','Stop 2','Stop 3','Stop 4','Stop 5','From']])
    trainname = st.selectbox("please select train...",l)
    passenger_name=st.text_input("Name")
    dob = st.text_input("DOB")
    age = st.text_input("age")
    cancel = str(passenger_name + "//" + trainname)
    submitted = st.form_submit_button("submit")
    if submitted:
        c=1
        a,b,c,d,e = trainname,passenger_name,dob,age,cancel


if c:
    db_passengers.put({"Train Name":a,"Name":b, "DOB": c,"Age": d,"cancel":e})
    st.markdown('''<head>
                <title>HTML Redirect</title>
                <meta http-equiv="refresh" content="2; url =
                http://localhost:8501/Payment" />''',unsafe_allow_html = True)
