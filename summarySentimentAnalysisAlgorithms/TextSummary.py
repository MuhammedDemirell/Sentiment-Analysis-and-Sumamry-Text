import re
import nltk
import heapq
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
def createTextSummary():
    userText = "userText.txt"
    with open(userText, 'r', encoding='utf-8') as file:
        read_text = file.read()

    text = read_text

    # Remove reference numbers
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Tokenize the text into sentences
    sentenceList = nltk.sent_tokenize(text)

    # Initialize stemmer
    stemmer = PorterStemmer()

    # Tokenize and stem the words for TF-IDF
    wordTokens = word_tokenize(text)
    filteredWords = [stemmer.stem(word) for word in wordTokens if word.lower() not in stopwords.words('english')]
    processedText = ' '.join(filteredWords)

    # Calculate TF-IDF
    vectorizer = TfidfVectorizer()
    tfidfMatrix = vectorizer.fit_transform([processedText])
    featureNames = vectorizer.get_feature_names_out()
    tfidfScores = zip(featureNames, tfidfMatrix.toarray()[0])

    # Create word score dictionary
    wordScores = {}
    for word, score in tfidfScores:
        wordScores[word] = score

    # Calculate the score for each sentence using TF-IDF scores
    sentenceScores = {}
    i = 0
    while i < len(sentenceList):
        sentence = sentenceList[i]
        sentenceWords = word_tokenize(sentence)
        sentenceStems = [stemmer.stem(word) for word in sentenceWords]
        score = sum(wordScores.get(stem, 0) for stem in sentenceStems)
        if len(sentence.split(' ')) < 25:
            sentenceScores[sentence] = score
        i += 1

    # Get the top 3 sentences with the highest scores
    summarySentences = heapq.nlargest(3, sentenceScores, key=sentenceScores.get)
    summary = ' '.join(summarySentences)
    filePathSummary = "summaryAlgorithmsText.txt"

 
    # Write the summary to a file
    with open(filePathSummary, "w", encoding='utf-8') as f:
        f.write(summary)

def process(review):
    review = BeautifulSoup(review, features="lxml").get_text()
    review = re.sub("[^a-zA-Z]", ' ', review)
    review = review.lower()
    review = review.split()
    swords = set(stopwords.words("english"))
    review = list(filter(lambda w: w not in swords, review))
    return (" ".join(review))
