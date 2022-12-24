# Import
import csv
import streamlit as st
import pandas as pd
from deta import Deta
import streamlit as st
import streamlit_authenticator as stauth
st.set_page_config(initial_sidebar_state="collapsed")
#st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

# CSS
page_image="""
<style>

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

# Deta Connection and Functions
DataKey = 'd05gnskf_zBRSkEhbeCFKcaKFwZHLopyWodKwN32b'
DataKey_Trains = 'd05gnskf_K83euLqNybw5SDKVvEMgxYTBs4y7n966'
Datakey_passengers = 'd05gnskf_AMQg96QfvUkNB1SBq9ExVWRnLCg5KM8J'

deta = Deta(DataKey)
deta_Trains = Deta(DataKey_Trains)
deta_passengers = Deta(Datakey_passengers)

db = deta.Base("loginDB")
db_trains = deta_Trains.Base("TrainsDB")
db_passengers = deta_passengers.Base("passengersDB")

# Login DB Functions
def insert_user(name,username,password,mailid):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"name":name, "username": username,"pwd": password,"mailid": mailid})

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items


def get_user(key):
    """If not found, the function will return None"""
    return db.get(key)

def delete_user(key):
    """Always returns None, even if the key does not exist"""
    return db.delete(key)

#Passengers
def fetch_all_passengers():
    res_passengers = db_passengers.fetch()
    return res_passengers.items

#Train DB Functions
def add_train():
    with st.form("Train Details"):
        name = st.text_input("Train Name")
        From = st.text_input("From Station")
        stop1 = st.text_input("1st Stop Station")
        stop2 = st.text_input("2nd Stop Station")
        stop3 = st.text_input("3rd Stop Station")
        stop4 = st.text_input("4th Stop Station")
        stop5 = st.text_input("5th Stop Station")
        To = st.text_input("To Station")
        arrtime = st.text_input("Arrival Time in the format hh:mm in 24hrs format")
        deptime= st.text_input("Departure Time in the format hh:mm in 24hrs format")
        duration= st.text_input("Duration of journey in hours")
        ac1 = st.slider('Number of seats in AC 1st Tier', 50, 120)
        ac2 = st.slider('Number of seats in AC 2nd Tier', 50, 150)
        ac3 = st.slider('Number of seats in AC 3rd Tier', 50, 150)
        sleep = st.slider('Number of seats in sleeper', 100, 200)
        button= st.form_submit_button(label="submit")
        if button:
            c=0
            for i in (name,From,stop1,stop2,stop3,stop4,stop5,To,arrtime,deptime,duration,ac1,ac2,ac3,sleep):
                if i == "":
                    st.warning("please fill the above fields")
                    c=1
                    break
            else:
                TrainDetails = {"Train Name":name, "From":From, "Stop 1":stop1, "Stop 2":stop2, "Stop 3":stop3, "Stop 4":stop4, "Stop 5":stop5, "To":To, "Arrival Time":arrtime, "Departure Time":deptime,"Duration":duration,"AC 1st Tier":ac1, "AC 2nd Tier":ac2,"AC 3rd Tier":ac3,"Sleeper":sleep}
                if c==0:
                    st.success("Train added succesfully!")
                    db_trains.put(TrainDetails)
                    st.markdown('''<head>
                            <title>HTML Redirect</title>
                            <meta http-equiv="refresh" content="0.5; url =
                            http://localhost:8501/Admin" />
                        </head>''',unsafe_allow_html=True)

def fetch_all_trains():
    res_trains = db_trains.fetch()
    return res_trains.items

def delete_train(key_train):
    return db_trains.delete(key_train)

def modify_train(uptrain,date,arrtime,deptime):
    keyname_train = df_trains[['Train Name','key']]
    update = st.button("update")
    for i in range(len(keyname_train)):
        if uptrain == keyname_train['Train Name'][i]:
            key_train = keyname_train['key'][i]
    if update:
        st.success("Updated!")
        st.markdown('''<head>
                    <title>HTML Redirect</title>
                    <meta http-equiv="refresh" content="0.5; url =
                    http://localhost:8501/Admin" />
                    </head>''',unsafe_allow_html=True)   
        return db_trains.update({"Date":date,"Arrival Time":arrtime,"Departure Time":deptime},key_train)
 
users = fetch_all_users()
trains = fetch_all_trains()
passengers = fetch_all_passengers()

def load_data():
    return pd.DataFrame(users)

def load_data_train():
    return pd.DataFrame(trains)

def load_data_passengers():
    return pd.DataFrame(passengers)

st.markdown("<p class='big-font'>Admin Portal</p>", unsafe_allow_html=True)


#User details
with st.container():
    logout = st.button("Sign out")
    if logout:
        st.markdown('''<head>
                    <title>HTML Redirect</title>
                    <meta http-equiv="refresh" content="0.5; url =
                    http://localhost:8501/Login" />
                    </head>''',unsafe_allow_html=True)
    with st.container():
        user_col1,user_col2 = st.columns(2)
        with user_col1:
            df = load_data()
            st.header("Users")
            df2=df[['name','username','mailid']]
            st.dataframe(df2)

    with st.container():    
        with user_col2:
            st.header("Manipulate User Data")
            user_l=['please select...','Delete user','Insert User','get User']
            opt_user = st.selectbox("please select...",user_l)
            if opt_user == user_l[1]:
                deluser = st.text_input("Name of the user whose account is to be deleted")
                delete= st.button("Delete")
                keyname = df[['name','key']]
                for i in range(len(keyname)):
                    if deluser == keyname['name'][i]:
                        key = keyname['key'][i]
                if delete:
                    delete_user(key)
                    st.markdown('''<head>
                            <title>HTML Redirect</title>
                            <meta http-equiv="refresh" content="0.5; url =
                            http://localhost:8501/Admin" />
                        </head>''',unsafe_allow_html=True)

            if opt_user == user_l[2]:
                with st.form("Insert user"):
                    name = st.text_input("Name")
                    username = st.text_input("Username")
                    mailid = st.text_input("Mail ID")
                    check=0
                    for i in ('@gmail.com','@outlook.com','@yahoo.com','@yandex.com','@icloud.com'):
                        if i in mailid:
                            check = 1
                    if mailid !='':
                        if check != 1:
                            st.warning('Invalid Email ID')
                    password = st.text_input("Password")
                    button= st.form_submit_button(label="submit")
                    if button:
                        c=0
                        for i in (name,username,mailid,password):
                            if i == "":
                                st.warning("please fill the above fields")
                                c=1
                                break
                        else:
                            if c==0:
                                st.success("Signed up")
                                insert_user(name,username,mailid,password)
                                st.markdown('''<head>
                                        <title>HTML Redirect</title>
                                        <meta http-equiv="refresh" content="0.5; url =
                                        http://localhost:8501/Admin" />
                                    </head>''',unsafe_allow_html=True)

            if opt_user == user_l[3]:
                getuser = st.text_input("Name of the user whose details are to be fetched")
                fetch= st.button("fetch")
                keyname = df[['name','key']]
                for i in range(len(keyname)):
                    if getuser == keyname['name'][i]:
                        key = keyname['key'][i]
                if fetch:
                    s = get_user(key)
                    table = pd.DataFrame(s,index=["1"])
                    st.dataframe(table[['username','name','mailid']])
        
#Train Details

with st.container():
    st.header("Train Details")
    df_trains = load_data_train()
    df_trains2 = df_trains[['Train Name','From','Stop 1','Stop 2','Stop 3','Stop 4','Stop 5','To','Arrival Time','Departure Time','Duration','AC 1st Tier','AC 2nd Tier','AC 3rd Tier','Sleeper']]
    st.dataframe(df_trains2)
    train_l=['Please Select...','Delete Train','Add Train','Modify departure Time',]
    opt_train = st.selectbox("please select...",train_l)
    if opt_train == train_l[1]:
        deltrain = st.text_input("Name of the train that is to be deleted")
        deletetrain= st.button("Delete")
        keyname_train = df_trains[['Train Name','key']]
        for i in range(len(keyname_train)):
            if deltrain == keyname_train['Train Name'][i]:
                key_train = keyname_train['key'][i]
                if deletetrain:
                    delete_train(key_train)
                    st.markdown('''<head>
                                <title>HTML Redirect</title>
                                <meta http-equiv="refresh" content="0.5; url =
                                http://localhost:8501/Admin" />
                                </head>''',unsafe_allow_html=True)
    if opt_train == train_l[2]:
        add_train()
    if opt_train == train_l[3]:
        uptrain = st.text_input("Name of the train whose details is to be updated")
        date = st.text_input("New date in the dd/mm/yyyy format")
        arrtime = st.text_input("New Arrival Time in the hh:mm 24hrs format")
        deptime = st.text_input("New Departure Time in the hh:mm 24hrs format")
        modify_train(uptrain,date,arrtime,deptime)

with st.container():
    st.header("Passenger Details")
    df_passengers = load_data_passengers()
    df_passengers2 = df_passengers[['Name','Train Name','DOB','Age']]
    st.dataframe(df_passengers2)