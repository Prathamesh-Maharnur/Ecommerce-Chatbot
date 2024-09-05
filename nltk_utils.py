import nltk
import numpy as np

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.tokenize.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words),dtype=np.float32)

    for idx,w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag

# sentence = ["hello","how","are","you"]
# all_words = ["hi","hello","I","you","bye","thank","cool"]
# bag = []
# bag = bag_of_words(sentence,all_words)
# print(bag)


# a = "How are you?"
# print(a)
# a = tokenize(a)
# print(a)

# words = ["Organize", "organizes", "organizing"]
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)