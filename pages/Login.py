# Import
import streamlit as st

# Data
trains={'CCExpress':['Chennai','a','b','c','d','Erode','Coimbatore'],'CMExpress':['Chennai','e','f','g','h','Madurai']}

def login():
    menu=['Admin','User']
    choice=st.selectbox("Please select...",menu)
    if choice=='User':
        username=st.text_input("user id: ")
        password=st.text_input("password: ",type="password")
        if username=='' or password=='':
            pass
        elif username=='railway' and password=='irctc':
            st.success("Logged in as {}".format(username))
            st.session_state['loggedin'] = True
            if st.session_state['loggedin']:
                booking()
            else:
                login()
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

def booking():
    st.write("## Welcome!")
    book,cancel = st.columns(2)

    with book:
        st.write("Go ahead and book tickets for your amazing journey")
        book_button = st.button("Book Tickets")
        if book_button:
            train_detail()

    with cancel:
        st.write("Want to cancel the tickets you booked earlier?")
        cancel_button = st.button("Cancel Tickets")

def train_detail():
    l=[]
    departure = st.text_input("Enter the place of departure")
    destination = st.text_input("Enter the destination")
    search=st.button("Search")
    if search:
        for i in trains:
            for j in trains[i]:
                if departure == j:
                    c = 1
                else:
                    c = 0
                if destination == j:
                    c2 = 1
                else:
                    c2 = 0
            if c2 and c:
                l.append(i)
    
        train=st.selectbox("Please select the train of your choice...",l) 

# Login
if 'loggedin' not in st.session_state:
    st.session_state['loggedin'] = False
    login()
else:
    if st.session_state['loggedin']:
        booking()
    else:
        login()


