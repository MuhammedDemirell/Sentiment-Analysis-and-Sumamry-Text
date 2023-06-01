import streamlit as st
import TextSummaryV2 as ts
import SummarySentimentAnalysis as ssa
import time
import matplotlib.pyplot as plt

def main():
    st.header("summarySentimentAnalysisAlgorithmsV2 Metin Özet ve Duygu Analizi Uygulaması")
    st.warning("Girdiğiniz metinler uzun cümlelerden ve noktalama işareleri olmamasından dolayı yanlış sonuçlar verebilir")
    # Sekmeleri oluşturma
    tabs = ["Metin Yazma"]
    choice = st.sidebar.selectbox("İşlev Seçin", tabs)

    if choice == "Metin Yazma":
        text = st.text_area("Metin yazın", height=200)

        if st.button("Gönder"):
            with open("userText.txt", "w", encoding="utf-8") as file:
                file.write(text)

            # Metnin özetini çıkar
            ts.createTextSummary()
            filePath="summaryAlgorithmsText.txt"
            ssa.process(filePath)

            # Özet dosyasını oku ve ekrana yazdır
            with open("summaryAlgorithmsText.txt", "r", encoding="utf-8") as summary_file:
                summary = summary_file.read()
                st.write("Gönderilen Metnin Özeti:")
                st.write(summary)
            with st.spinner("Metin analiz ediliyor..."):
                countdown_placeholder = st.empty()
                countdown_duration = 3
                for i in range(countdown_duration, 0, -1):
                    countdown_placeholder.write(f"Sonuçlar hazırlanıyor... {i} saniye kaldı")
                    time.sleep(1)
                countdown_placeholder.empty()

                prediction = ssa.predictSentiment()
                st.write("Metnin olumlu olma olasılığı:", prediction)
                st.write("Metnin olumsuz olma olasılığı:", (1 - prediction))

                # Grafik oluşturma ve gösterme
                fig, ax = plt.subplots()
                models = ['Positive', 'Negative']
                scores = [prediction, 1 - prediction]
                colors = ['tab:green', 'tab:red']
                ax.bar(models, scores, color=colors)
                ax.set_ylim([0, 1])
                ax.set_title("Score for Sentiment Analysis Models")
                ax.set_xlabel("Sentiment Analysis")
                ax.set_ylabel("Score (out of 1)")
                st.pyplot(fig)


if __name__ == '__main__':
    main()
