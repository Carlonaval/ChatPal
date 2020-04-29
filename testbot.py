import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np 
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
f = open('chatbot.txt', 'r', errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"

raw = f.read()
raw = raw.lower()

nltk.download('punkt') 
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)# converting the file to a list of sentences
word_tokens = nltk.word_tokenize(raw)# converting the sentences list to words
sent_tokensone = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokensone = nltk.word_tokenize(raw)

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()

def lemmerTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
no_punct = dict((ord(punct), None) for punct in string.punctuation)

def lemNormalized(text):
    return lemmerTokens(nltk.word_tokenize(text.lower().translate(no_punct)))

normal_greetings_in = ("hello", "hi", "greetings")
normal_greetings_out = ["hi", "how may I help you?", "hello! what do you need help for?"]

#returning a greeting 
def greeting(sentence): 
    for word in sentence.split():
        if word.lower() in normal_greetings_in:
            return random.choice(normal_greetings_out)

#checking for quesiton
def basicM(sentence):
    for word in normal_greetings_in:
        if sentence.lower() == word:
            return random.choice(normal_greetings_out)


def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    bot_response = ''
    sent_tokens.append(user_response)

    TfidVec = TfidfVectorizer(tokenizer = lemNormalized, stop_words = 'english')
    tfidf = TfidVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf == 0):
        bot_response = bot_response + "I am sorry! I don't understand."
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response

    

def chat(user_response):
    user_response=user_response.lower()
    keyword = " chatbot "
    keywordone = " chatbot "
    keywordsecond = " chatbot "

    flag = True
    print("I will provide answers to your queries about CPE Program. If you wish to exit, type quit!")

    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag=False
            return "You are welcome"
        elif(basicM(user_response)!=None):
            return basicM(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                return response(user_response)
                sent_tokensone.remove(user_response)
            elif(greeting(user_response)!=None):
                return greeting(user_response)
            elif(user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif(basicM(user_response)!=None):
                return basic(user_response)
            else: 
                return response(user_response)
                sent_tokens.remove(user_response)


    else:
        flag=False
        return "Bye! Have a great day."         







