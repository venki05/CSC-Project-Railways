import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
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
    font-size:50px !important;
    color: black
}

.medium-font {
    font-size:35px !important;
    color: black
}

.small-font{
    font-size:15px !important;
    color: black
}
</style>
""", unsafe_allow_html=True)

def about():
    st.markdown("<p class='big-font'>About us</p>",unsafe_allow_html = True)
    st.markdown("<p class='small-font'>Retro Railways is a website for railway ticket booking to any place around India. </p>",unsafe_allow_html = True)
    st.markdown("<p class='small-font'>Formed in 2021 it is your GO-TO WEBSITE for TRAIN Ticket BOOKING. </p>",unsafe_allow_html = True)
    st.markdown("<p class='medium-font'>ADDRESS:",unsafe_allow_html = True)
    st.markdown("<p class='small-font'>Retro Railways, </p>",unsafe_allow_html = True)
    st.markdown("<p class='small-font'>5th Cross Street  Besant Nagar </p>",unsafe_allow_html = True)
    st.markdown("<p class='small-font'>For any further queries contact us at: </p>",unsafe_allow_html = True)
    st.markdown("<p class='small-font'>GMAIL: retrorailways@gmail.com</p>",unsafe_allow_html = True)
    st.markdown("<p class='small-font'> CONTACT NUMBER : 98456 00743</p>",unsafe_allow_html = True)

about()

