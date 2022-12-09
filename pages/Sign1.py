#imports
import streamlit as st
from deta import Deta
import pandas as pd

# Page setup
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
DataKey_Trains = 'd05gnskf_K83euLqNybw5SDKVvEMgxYTBs4y7n966'
deta_Trains = Deta(DataKey_Trains)
db_trains = deta_Trains.Base("TrainsDB")

#Functions
def passenger():
    passenger_name= st.text_input("Passenger Name")
    dob =st.text_input("Date of Birth in dd/mm/yyyy format")
    age = st.text_input("Age")
    Enter = st.button("Enter")
    if passenger_name =='' or dob == '' or age == '':
        pass
    if Enter:
        st.write("Payment")



def fetch_all_trains():
    res_trains = db_trains.fetch()
    return res_trains.items    

def details():
    #Train Details from User
    l=[]
    From = st.text_input("From")
    To = st.text_input("To")
    date=st.text_input("Date of Journey in the format dd/mm/yyyy")
    submit = st.button("Submit")
    if submit:
        st.markdown('''<head>
            <title>HTML Redirect</title>
            <meta http-equiv="refresh" content="0.5; url =
            http://localhost:8501/Sign1" />
            </head>''',unsafe_allow_html=True)

def download():
    from fpdf import FPDF
 
    # Create instance of FPDF class
    # Letter size paper, use inches as unit of measure
    pdf=FPDF(format='letter', unit='in')
    
    # Add new page. Without this you cannot create the document.
    pdf.add_page()
    
    # Remember to always put one of these at least once.
    pdf.set_font('Times','Train Ticket',10.0) 
    
    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin
    
    # Set column width to 1/4 of effective page width to distribute content 
    # evenly across table and page
    col_width = epw/4
    
    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    
    data=[["passenger name","venki"],
    ["passenger phone number","9876543276"],
    ["pnr number","1234"],
    ["train name","shadabdhi 123AO"],
    ["from","chennai"],
    ["to","pune"],
    ["date of journey","12/12/2022"]
    ]

    # Text height is the same as current font size
    th = pdf.font_size
    
    
    # Line break equivalent to 4 lines
    pdf.ln(4*th)
    
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(0.5)
    
    # Here we add more padding by passing 2*th as height
    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(datum), border=1)
    
        pdf.ln(2*th)
    
    pdf.output('table-using-cell-borders.pdf','F')

trains = fetch_all_trains()
pd_train = pd.DataFrame(trains)
pd2_train = pd_train[['Train Name','To','Stop 1','Stop 2','Stop 3','Stop 4','Stop 5','From']]
with st.form("book"):
    From = st.text_input("From")
    To = st.text_input("To")
    submitted = st.form_submit_button(label="Submit")
if submitted:
    l=[]
    for i in trains:
        s=(i['To'],i['Stop 1'],i['Stop 2'],i['Stop 3'],i['Stop 4'],i['Stop 5'],i['From'])
        if From in s and To in s:
            df = pd.DataFrame(i,index=[""])
            l.append(i['Train Name'])
            st.write(df[['Train Name','To','Stop 1','Stop 2','Stop 3','Stop 4','Stop 5','From']])
    if l != []:
        select_train = st.selectbox("Please select the train...",l)
        num_tickets = st.slider("number of tickets",1,8)
        for i in range(num_tickets):
            passenger()
    else:
        st.warning("No trains are available on that day. Please select some other day")
