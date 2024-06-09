import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Set up the page
st.set_page_config(page_title="Shifas Aslam S - Portfolio", page_icon=":bar_chart:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/f36de2d0-57b0-49e2-b213-2b3c85b12336/ItUEJHPoSr.json")
# image = Image.open("")
st.write("##")
st.subheader("Welcome to my Portfolio :wave:")
st.title("Shifas Portfolio Website")
st.write("""
    **About Me**

    I am a recent graduate with a strong passion for data analysis. 
    I have a solid foundation in statistics, data visualization, 
    and programming languages like Python and SQL. 
    My skills include transforming raw data into meaningful insights to support decision-making.
    I am eager to apply my analytical skills and learn from real-world experiences. 
    I am enthusiastic about starting my career as a data analyst and contributing to impactful projects.
""")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write('##')
            st.subheader("Hello! I'am Shifas Aslam")
            st.write("Passionate about uncovering insights through data analysis, I strive for simplicity and elegance in every insight revealed.")
        with col2:
            st_lottie(lottie_coder)

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education:")
            st.write("- B.Sc Information Technology")
        with col4:
            st.subheader("Experience:")
            st.write("- 3 Month as Junior Trainee Odoo Developer")

    st.write("---")
    

    st.download_button(
        label="Download Resume",
        data=open("/home/dell/my_portfolio/Resume Shifas Aslam S (8).pdf", "rb"),
        file_name="Shifas_Aslam_Resume.pdf",
        mime="application/pdf"
    )

if selected == "Projects":
    with st.container():
        st.header("My Projects")
        # st.write("##")
        st.write("""
                 Developed a YouTube data harvesting project to analyze 
                 trends, user engagement, and content performance,
                leveraging API integration and data visualization techniques.
                 """)
        col5, col6 = st.columns((1, 2))
        # with col5:
        #     st.image(image)
        with col6:
            st.markdown("[Visit my GitHub](https://github.com/shifas-aslam/Youtubedataharevesting.git)")

if selected == "Contact":
    st.header("Get in touch!")
    # st.write("##")
    # st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/shifasaslam01@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)



