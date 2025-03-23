import pyttsx3
import streamlit as st

def text_to_speech(text, speed):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set the speech rate based on user selection
        engine.setProperty('rate', speed)
        
        # Queue the text for speaking
        engine.say(text)

        # Process and output the speech
        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")

# Streamlit UI
st.title("SRQ Text To Speech App")

# User input text
user_input = st.text_input("Enter Script To Speak")

# Radio button to select speech speed
genre = st.radio(
    "Select Speed Of Speech",
    ["0.5x", "1.0x", "1.5x"],
    captions=[
        "Slower Than Usual",
        "Default",
        "Faster Than Usual",
    ],
)

# Mapping selected speed to actual speech rates
speed_map = {
    "0.5x": 100,  # Slower
    "1.0x": 150,  # Default
    "1.5x": 200,  # Faster
}
selected_speed = speed_map[genre]

# Speak when user enters text
if user_input:
    text_to_speech(user_input, selected_speed)

# Button to repeat speech
if st.button("Tap To Speak Again"):
    text_to_speech(user_input, selected_speed)
