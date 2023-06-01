import streamlit as st
import speech_recognition as sr
def audioRecognitions(uploaded_audio):
    r = sr.Recognizer()
    recognizedText = ""

    with sr.AudioFile(uploaded_audio) as source:
        audioData = r.record(source)
        try:
            text = r.recognize_google(audioData, language="en-US")
            recognizedText += text + " "
        except:
            st.warning("Ses Dosyası Anlaşılamadı.")

    with open(
            "allTexts/AudioRecognitions.txt",
            mode='w') as file:
        file.write(recognizedText)

    return recognizedText