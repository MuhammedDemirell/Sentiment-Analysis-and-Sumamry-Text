import pandas as pd
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

import re

# Veri okuma
data = pd.read_csv(r"C:\Users\PC\Desktop\son\Sentiment-Analysis\dataSet\NLPDataSet.tsv", delimiter="\t", quoting=3)


# Metin ön işleme işlemleri
def process(review):
    review = BeautifulSoup(review, features="lxml").get_text()
    review = re.sub("[^a-zA-Z]", ' ', review)
    review = review.lower()
    review = review.split()
    swords = set(stopwords.words("english"))
    review = [w for w in review if w not in swords]
    return (" ".join(review))


# Veri kümesinin işlenmesi
dataArray = []
for i in range(len(data["review"])):
    if (i + 1) % 1000 == 0:
        print(f"{i + 1} reviews processed...")
    dataArray.append(process(data["review"][i]))

# Veri kümesinin eğitim ve test olarak ayrılması
trainData, testData, trainLabels, testLabels = train_test_split(dataArray, data["sentiment"], test_size=0.7,
                                                                random_state=33)

# Özellik çıkarımı
vectorizer = CountVectorizer(max_features=5000)
trainDataVectorized = vectorizer.fit_transform(trainData)
trainDataVectorized = trainDataVectorized.toarray()

testDataVectorized = vectorizer.transform(testData)
testDataVectorized = testDataVectorized.toarray()

# Model eğitimi
rf = RandomForestClassifier(n_estimators=140, n_jobs=-1)
rf.fit(trainDataVectorized, trainLabels)  # Fit the classifier to the training data

testPredict = rf.predict(testDataVectorized)
analysis = roc_auc_score(testLabels, testPredict)
print(analysis)
