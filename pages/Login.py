# Import
import streamlit as st

# Data
stations=['please select','Chennai','Coimbatore','Madurai','Trichy','Kanyakumari']
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
            return True
        else:
            st.error("Login credenials are wrong")
            return False
    

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
    book,space,space2,cancel = st.columns(4)

    with book:
        st.write("Go ahead and book tickets for your amazing journey")
        book_button = st.button("Book Tickets",on_click = train_detail())


    with space:
        pass

    with space2:
        pass

    with cancel:
        st.write("Want to cancel the tickets you booked earlier?")
        cancel_button = st.button("Cancel Tickets")

def train_detail():
    l=[]
    departure = st.selectbox("Departure",stations)
    if departure != 'please select':
        destination = st.selectbox("Destination",stations)
    search=st.button("Search")
    if search:
        for i in trains:
            for j in trains[i]:
                st.write(j)
                if departure == j:
                    c = 1
                else:
                    c = 0
                if destination == j:
                    c2 = 1
                else:
                    c2 = 0
            if c2 == 1 and c == 1:
                l.append(i)
    
        rail=st.selectbox("Please select the train of your choice...",l) 

# Login

session = login()
if session:
    booking()


