import nltk
import numpy as np 
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
f = open('chatbot.txt', 'r', errors = 'ignore')
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

print(sent_tokens)
print(word_tokens)

lemmer = nltk.stem.WordNetLemmatizer()

def lemmerTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
no_punct = dict((ord(punct), None) for punct in string.punctuation)

def lemNormalized(text):
    return lemmerTokens(nltk.word_tokenize(text.lower().translate(no_punct)))

normal_greetings_in = ("hello", "hi", "greetings")
normal_greetings_out = ["hi", "how may I help you?", "hello! what do you need help for?"]
Basic_Om = ['tuition']
Basic_AnsM = ['The tuition is around P30-40k per term.']

#returning a greeting 
def greeting(sentence): 
    for word in sentence.split():
        if word.lower() in normal_greetings_in:
            return random.choice(normal_greetings_out)

#checking for quesiton
def basicM(sentence):
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)


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

def response1(user_response):
    bot_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=lemNormalized, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response
    

def chat(user_response):
    user_response=user_response.lower()
    keyword = " module "
    keywordone = "module "
    keywordsecond = " module "

    flag = True
    print("BOT: I will provide answers to your queries about CPE Program. If you wish to exit, type quit!")

    while(flag==True):
        user_response = input()
        user_response = user_response.lower()
        if(user_response != 'quit'):
            if(user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print("BOT: You're welcome! Have a nice day.")
            else:
                if(greeting(user_response) != None):
                    print("BOT: "+greeting(user_response))
                else:
                    print("Bot: ", end="")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag = False
            print("BOT: See you later!")
    


