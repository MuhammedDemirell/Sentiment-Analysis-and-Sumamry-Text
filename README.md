# Duygu Analizi ve Metin Özeti

Film ve dizilerin yorumları analiz edilmiştir. Gireceğiniz metin veya istediğiniz özet , Streamlit'in ana sayfasında yönlendirilmeler yapılmıştır. 
Uygulamayı çalıştırmak için her klasörün bulunduğu dizine giderek terminalde aşağıdaki komutu kullanabilirsiniz:

"streamlit run UserPage.py"

## Klasör Açıklamaları

- **sentimentAnalysis**: Bu klasörde konuşma veya ses kaydını metine çevirmektedir, sonrasında duygu analizi yapılmaktadır.
- **sentimentAnalysisV2**: Bu klasörde girilen metnin duygu analizi yapılmaktadır.
- **summarySentimentAnalysisAlgorithms**: Bu klasörde girilen metnin özeti çıkarılır ve duygu analizi yapılmaktadır.
- **summarySentimentAnalysisAlgorithmsV2**: Bu klasörde kendim hazırladığım ve denediğim algoritma kullanılmıştır. Metnin özetini çıkarır ve duygu analizi yapılmaktadır.

**Not:** Kullanılan sürümler uyumsuz olması durumunda modül hataları oluşabilir. Sorunu çözmek için `process` fonksiyonundan `-features="lxml"` özelliğini kaldırabilirsiniz.



# Sentiment Analysis and Summary Text

Film and series reviews have been analyzed. You can enter text or request a summary, and the application will redirect you to the homepage of Streamlit.
To run the application, navigate to the directory where each folder is located in the terminal and type the following command:

"streamlit run UserPage.py"

## Folder Descriptions

- **sentimentAnalysis**: This folder converts speech or audio recordings into text and then performs sentiment analysis.
- **sentimentAnalysisV2**: This folder performs sentiment analysis on the entered text.
- **summarySentimentAnalysisAlgorithms**: This folder extracts a summary of the entered text and performs sentiment analysis.
- **summarySentimentAnalysisAlgorithmsV2**: This folder uses an algorithm I have developed and tested. It extracts a summary of the text and performs sentiment analysis.

**Note:** If the versions used are incompatible, it may cause a module error. To resolve this issue, you can remove the `-features="lxml"` attribute from the process function.



