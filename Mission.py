import streamlit as st
from PIL import Image
from io import BytesIO

# Custom CSS to inject into the Streamlit app
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to check answers and return the result
def check_answer(question, user_answer):
    correct_answers = {
        1: 'B',
        2: 'A',
        3: 'C',
        4: 'A',
        5: 'B',
        6: 'B'
    }
    return user_answer == correct_answers[question]

# Function to display the quiz


# ---- HEROES SECTION ----

def app():
    local_css("style/style.css")  # Path to your CSS file

    with st.container():
     st.write("---")
     st.header("Missions")
     st.write("##")
    img_contact_form = Image.open("images/yt_contact_form.png")
    audio = "audio/Superman.mp3"
        
        
    st.image(img_contact_form)  # Replace with the path to your hero image
        
    st.subheader("Superman and 3R Protectors Save the World")
    st.write(
                """
          In the bustling city of Metropolis, where skyscrapers touch the clouds and the streets buzz with life, there lived heroes of all kinds. Among them was Superman, soaring through the sky, a beacon of hope and courage. But in this city, not all heroes wore capes. Some were smaller, nimbler, and just as mighty—they were the **3R Protectors**.

         One sunny day, as Superman patrolled the city, he spotted something unusual. It wasn't a bird or a plane, but a mountain of trash so high it nearly scraped the sky! This was Mount Littermore, a colossal heap of waste that cast a shadow over Metropolis.

          Superman knew this was no job for one hero alone. He needed the mightiest force of all—the 3R Protectors, a band of kids with hearts as pure as the planet they vowed to protect.

         🌟 **RecycloGirl**, with her cape made of recycled plastic, led the charge. She could spot a recyclable a mile away and transform it into something magical!

         🧙 **ReuseWizard**, with his wand of repurposed wood, waved it with a flourish, giving old things new life and purpose.

         🚀 **ReductoKid**, the thinker of the trio, always had a plan to cut waste down to size, making sure nothing more than needed was used.

         Together with Superman, they hatched a plan as brilliant as the stars. They organized grand clean-up festivals, where everyone sang and danced while picking up litter. They crafted workshops where trash turned into treasure, and they spread the word far and wide about the power of reducing waste.

         Superman, with a gust of his super-breath, sent reusable bottles and bags fluttering into the hands of every citizen. And lo and behold, as the people of Metropolis joined hands with the 3R Protectors, Mount Littermore began to shrink!

         Parks sparkled, rivers sang clear melodies, and the air was sweet once more. The 3R Protectors had shown that even the smallest hands could turn the tide.

         And so, children everywhere learned that they, too, could be heroes. With a pledge to recycle, reuse, and reduce, they could save their world, one small step at a time. And Superman? He smiled, knowing the true power of a hero was the legacy they inspired in others.
         and happy to know that you are the member of webvengers. Do not forget to answer the upcoming activity to boost your strength

               
                """
            )

        # Load your audio file
    audio_bytes = open(audio, 'rb').read()

        # Use st.audio to play the audio
    st.audio(audio_bytes, format='audio/mp3')

        # Add some interactive elements for gamification
    if st.button('Join the 3R Protectors!'):
            st.balloons()
            st.write("Welcome to the team! Let's save the world together.")




def display_quiz():
    st.title("The Adventures of Superman and the 3R Protectors Quiz!")
    st.write("Welcome to the superhero quiz! Let's see how well you remember the story.")

    questions = {
        1: "What is the name of the mountain of trash in Metropolis?",
        2: "Who leads the 3R Protectors with a cape made of recycled plastic?",
        3: "What does ReuseWizard use to give old things new life?",
        4: "What did the people of Metropolis do at the grand clean-up festivals?",
        5: "What did Superman send fluttering into the hands of every citizen?",
        6: "What is the true power of a hero, according to Superman?"
    }
    
    options = {
        1: ['A) Mount Everest', 'B) Mount Littermore', 'C) Mount Trashmore', 'D) Mount Clean'],
        2: ['A) RecycloGirl', 'B) ReuseWizard', 'C) ReductoKid', 'D) Superman'],
        3: ['A) A magic hat', 'B) A recycling bin', 'C) A wand of repurposed wood', 'D) Super strength'],
        4: ['A) They sang and danced while picking up litter.', 'B) They watched movies.', 'C) They played video games.', 'D) They slept.'],
        5: ['A) Candy', 'B) Reusable bottles and bags', 'C) Money', 'D) Leaves'],
        6: ['A) The ability to fly', 'B) The legacy they inspire in others', 'C) Super strength', 'D) Invisibility']
    }

    score = 0
    for q_number in range(1, 7):
        st.subheader(f"Question {q_number}")
        st.write(questions[q_number])
        answer = st.radio("Choose one option:", options[q_number], key=str(q_number))
        
        if st.button(f'Submit Answer for Question {q_number}'):
            if check_answer(q_number, answer[0]):
                st.success("Correct!")
                score += 1
            else:
                st.error("Oops! That's not correct.")
    
    st.write(f"Your final score is {score}/6")
    if score == 6:
        st.balloons()




bt = st.button("Answer a Quiz")
if bt == True:
    display_quiz()
        