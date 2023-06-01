import streamlit as st
import speech_recognition as sr
import os


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-US')
        return text
    except:
        st.warning("Sesiniz Anlaşılamadı.")
        return None


def save_text(text):
    with open("allTexts/microphoneRecognitions.txt", "w") as f:
        f.write(text)
