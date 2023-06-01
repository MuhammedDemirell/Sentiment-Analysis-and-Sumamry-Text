import re
import nltk
import heapq

data = "textExam.txt"

with open(data, 'r', encoding='utf-8') as file:
    read_text = file.read()

text = read_text

# Remove reference numbers
text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Tokenize the text into sentences
sentenceList = nltk.sent_tokenize(text)

# Remove punctuation to find the most frequent words
wordText = re.sub('[^a-zA-Z]', ' ', text)
wordText = re.sub(r'\s+', ' ', wordText)

# Get the stopwords in English
stopWords = nltk.corpus.stopwords.words('english')

# Count word frequencies
wordFrequencies = {}
for word in nltk.word_tokenize(wordText):
    if word not in stopWords:
        if word in wordFrequencies.keys():
            wordFrequencies[word] += 1
        else:
            wordFrequencies[word] = 1

# Get the maximum word frequency
maxFrequency = max(wordFrequencies.values())


# Calculate the weighted frequency for each word
for word in wordFrequencies.keys():
    wordFrequencies[word] = (wordFrequencies[word] / maxFrequency)

# Calculate the score for each sentence
sentenceScores = {}
for sentence in sentenceList:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in wordFrequencies.keys():
            if len(sentence.split(' ')) < 25:
                if sentence in sentenceScores.keys():
                    sentenceScores[sentence] += wordFrequencies[word]
                else:
                    sentenceScores[sentence] = wordFrequencies[word]

# Get the top 7 sentences with the highest scores
summarySentences = heapq.nlargest(5, sentenceScores, key=sentenceScores.get)

summary = ' '.join(summarySentences)

# Write the summary to a file
f = open("TextSummaryV2.txt", "w")
f.write(summary)
f.close()
