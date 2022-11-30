import streamlit as st

trains={'CCExpress':['Chennai','a','b','c','d','Erode','Coimbatore'],'CMExpress':['Chennai','e','f','g','h','Madurai']}

def train_detail():
    l=[]
    departure = st.selectbox("Departure",trains)

def booking():
    st.write("Welcome!")
    book,space2,cancel = st.columns(3)
    with book:
        st.write("Go ahead and book tickets for your amazing journey")
        book_button = st.button("Book Tickets",on_click = train_detail())
    with space2:
        pass
    with cancel:
        st.write("Want to cancel the tickets you booked earlier?")
        cancel_button = st.button("Cancel Tickets")

booking()