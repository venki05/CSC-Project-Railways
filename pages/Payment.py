#Import
import streamlit as st

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
    
    pdf.output('E-Ticket','F')

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


st.header("Payment")
payment = st.selectbox("Enter Mode of payment",['please select...','Netbanking','Credit/Debit card','Paytm','GPay','Phonepe'])
if payment != 'please select...':
    st.success("Your transaction was successful!")
    st.write("The E-Ticket will be sent to your registered mail id within the next 3 hours. If you don't recieve your ticket even after 3 hours please contact our customer support")
    logout= st.button("Logout")
    if logout:
        st.markdown('''<head>
        <title>HTML Redirect</title>
        <meta http-equiv="refresh" content="0.5; url =
        http://localhost:8501/Login" />''',unsafe_allow_html = True)

