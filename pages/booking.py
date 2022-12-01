import streamlit as st

trains={'A Express':['Chennai','Madurai','Tirunelveli','thiruvaiyar','Rameswaram'],'B Express':['a','b','c','d']}
places=['Chennai','Madurai','Tirunelveli','thiruvaiyar','Rameswaram','a','b','c','d']
def train_detail():
    l=[]
    destination=st.selectbox("Destination",places)
    departure = st.selectbox("Departure",places)
    if departure!=destination:
        for i in trains.values():
            if departure in i[1] and destination in i[1]:
                l.append(i[0])
        train=st.selectbox(l)
    

def booking():
    st.write("Welcome!")
    book,space2,cancel = st.columns(3)
    with book:
        st.write("Go ahead and book tickets for your amazing journey")
        book_button = st.button("Book Tickets")
        if book_button:
            train_detail()
    with space2:
        pass
    with cancel:
        logout_button=st.button("Logout")
        st.write("Want to cancel the tickets you booked earlier?")
        cancel_button = st.button("Cancel Tickets")
        if logout_button:
            st.markdown('''<head>
    <title>HTML Redirect</title>
    <meta http-equiv="refresh" content="0.5; url =
    http://localhost:8501/Login" />
</head>''',unsafe_allow_html=True)

booking()