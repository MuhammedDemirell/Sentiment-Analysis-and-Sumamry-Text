import time
import streamlit as st
import sys
import time
import nltk
nltk.download('stopwords')

sys.path.append("..")
import MicrophoneRecognitions as mr
import AudioRecognitions as ar
import LanguageProcessingAudio as lpa
import LanguageProcessingSpeech as lps
import matplotlib.pyplot as plt


def matplotlibOutputAudio():
    models = ['Positive', 'Negative']
    scores = [lpa.prediction, 1 - lpa.prediction]
    colors = ['tab:green', 'tab:red']

    plt.bar(models, scores, color=colors)
    plt.ylim([0, 1])
    plt.title("Score for Sentiment Analysis Models")
    plt.xlabel("Sentiment Analysis")
    plt.ylabel("Score (out of 1)")
    plt.show()
    return st.pyplot()


def matplotlibOutputSpeech():
    models = ['Positive', 'Negative']
    scores = [lps.prediction, 1 - lps.prediction]
    colors = ['tab:green', 'tab:red']

    plt.bar(models, scores, color=colors)
    plt.ylim([0, 1])
    plt.title("Score for Sentiment Analysis Models")
    plt.xlabel("Sentiment Analysis")
    plt.ylabel("Score (out of 1)")
    plt.show()
    return st.pyplot()


def login():
    st.title("Kullanıcı Girişi")

    # Kullanıcı adı ve şifre alanları
    username = st.text_input("Kullanıcı Adı", key="username_input")
    password = st.text_input("Şifre", type="password", key="password_input")

    # Giriş yapma düğmesi
    if st.button("Giriş Yap", key="login_button"):
        if len(username) > 5 and len(password) > 5:
            st.success("Giriş Başarılı!")
            st.session_state.username = username
            st.session_state.logged_in = True
        else:
            st.error("Kullanıcı Adı ve Şifre En Az 5 Karakter Olmalıdır.")
            return False

    # Oturum açılmamışsa hata mesajı
    if not st.session_state.get("logged_in", False):
        return False

    return st.session_state.logged_in


if login():
    if "text" not in st.session_state:
        st.session_state.text = None

    # Kaydetme ve yükleme seçimi
    option = st.selectbox(
        "Lütfen Bir Seçenek Seçiniz:",
        ("Kaydet 🎤", "Yükle 📁")
    )

    if option == "Kaydet 🎤":
        # Kaydet butonu
        if st.button("Kaydet", key="record_button"):
            text = mr.recognize_speech()
            if text:
                st.session_state.text = text
                st.write("Anlaşılan Metin:")
                st.write(text)
                mr.save_text(text)
                filePath = "allTexts/microphoneRecognitions.txt"
                lps.process(filePath)
                # Natural language processing
                with st.spinner("Metin analiz ediliyor..."):
                    countdown_placeholder = st.empty()
                    countdown_duration = 3
                    for i in range(countdown_duration, 0, -1):
                        countdown_placeholder.write(f"Sonuçlar hazırlanıyor... {i} saniye kaldı")
                        time.sleep(1)
                    countdown_placeholder.empty()

                    prediction = lps.predict_sentiment()
                    st.write("Metnin olumlu olma olasılığı:", prediction)
                    st.write("Metnin olumsuz olma olasılığı:", (1 - prediction))

                    # Grafik oluşturma ve gösterme
                    graphics, plt = plt.subplots()
                    models = ['Positive', 'Negative']
                    scores = [prediction, 1 - prediction]
                    colors = ['tab:green', 'tab:red']
                    plt.bar(models, scores, color=colors)
                    plt.set_ylim([0, 1])
                    plt.set_title("Score for Sentiment Analysis Models")
                    plt.set_xlabel("Sentiment Analysis")
                    plt.set_ylabel("Score (out of 1)")
                    st.pyplot(graphics)

                st.success("Metin Başarıyla Kaydedildi.")


        # Daha önce kaydedilen metin varsa göster
        elif st.session_state.text:
            st.write("Daha Önce Kaydedilen Metin:")
            st.write(st.session_state.text)

        # Kaydedilen metin yoksa mesaj göster
        else:
            st.write("Henüz Kaydedilen Metin Yok.")

    elif option == "Yükle 📁":
        # Ses dosyası yükleme özelliği
        uploaded_audio = st.file_uploader("Ses Dosyası Yükle", type=["wav"])

        if uploaded_audio is not None:

            if st.button("Ses Dosyasını İşle", key="process_audio_button"):
                with st.spinner("Ses dosyası işleniyor..."):
                    recognized_text = ar.audioRecognitions(uploaded_audio)
                    if recognized_text:
                        st.write("Tanınan Metin:")
                        st.write(recognized_text)
                        filePath = "allTexts/AudioRecognitions.txt"
                        lpa.process(filePath)
                        # Natural language processing
                        with st.spinner("Metin analiz ediliyor..."):
                            countdown_placeholder = st.empty()
                            countdown_duration = 3
                            for i in range(countdown_duration, 0, -1):
                                countdown_placeholder.write(f"Sonuçlar hazırlanıyor... {i} saniye kaldı")
                                time.sleep(1)
                            countdown_placeholder.empty()

                            prediction = lpa.predict_sentiment()
                            st.write("Metnin olumlu olma olasılığı:", prediction)
                            st.write("Metnin olumsuz olma olasılığı:", (1 - prediction))

                            # Grafik oluşturma ve gösterme
                            graphics, plt = plt.subplots()
                            models = ['Positive', 'Negative']
                            scores = [prediction, 1 - prediction]
                            colors = ['tab:green', 'tab:red']
                            plt.bar(models, scores, color=colors)
                            plt.set_ylim([0, 1])
                            plt.set_title("Score for Sentiment Analysis Models")
                            plt.set_xlabel("Sentiment Analysis")
                            plt.set_ylabel("Score (out of 1)")
                            st.pyplot(graphics)


                    else:
                        st.error("Ses Dosyası İşlenemedi.")

    if st.session_state.get("logged_in", False):
        if st.button("Çıkış Yap", key="logout_button"):
            # Kullanıcı adı ve şifre alanlarını temizle
            st.session_state.username = ""
            st.session_state.logged_in = False
            st.warning("Oturum Sonlandırıldı.")
            time.sleep(1)
            st.experimental_rerun()
