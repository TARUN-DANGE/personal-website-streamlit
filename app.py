import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import Mission


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/9e95fff7-6b74-4fef-9302-35b8ef3d7843/JiUsmBC3gC.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    option = st.sidebar.selectbox("Gears",["PROFILE","MISSIONS","HEROES","ABOUT US"])
    st.subheader("WEBVENGERS:zap:")
    st.title("Webvengers Assemble Here :earth_asia:")
    st.write(
        "Get Ready to Dive in the Journey of Non-stop learning . Webvengers are here Now :superhero:"
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write("##")
        st.write(
            """
           Crafting the Webvengers Experience:

Age-appropriate challenges:  Design challenges with different difficulty levels for various age groups. Younger children can focus on basic problem-solving, while older kids can tackle more complex social dilemmas.

Variety is key:  Offer a mix of activities to keep things engaging. This could include quizzes, interactive stories, simulations, and even creative tasks where kids design their superhero solutions.

Storytelling power:  Embed problem-solving scenarios within a captivating superhero narrative. Maybe a villain is causing trouble in the city, and Webvengers need to use their skills to save the day.

Social good focus:  Clearly connect problem-solving with real-world social duties. Show kids how their actions as Webvengers can translate to helping others in their community.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Topics")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("How to Develop Our Thing Ability like Ironman #ProblemSolver")
        st.write(
            """
           In this series we will enhance our Brain power and with easy Quiz earn Power Xp
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/Sd9MZdB1ItU?si=Q940TJTnSFNSq19u)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("The Story to Establish the 3R away from City #Superman")
        st.write(
            """
            How the our hero cleans up our city the mistry behind 3R is here ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/OasbYWF4_S8?si=M8UMZ1jTYRT3rCvX)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
if option == 'MISSIONS':
    Mission.app()
    Mission.display_quiz()
