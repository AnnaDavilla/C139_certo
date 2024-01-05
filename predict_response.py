# Bibliotecas de pré-processamento de dados de texto
import nltk
nltk.download('punkt')
nltk.download('wordnet')

# palavras a serem ignoradas/omitidas ao enquadrar o conjunto de dados
ignore_words = ['?', '!',',','.', "'s", "'m"]

import json
import pickle

import numpy as np
import random

# Biblioteca load_model
import tensorflow
from data_preprocessing import get_stem_words

# carregue o modelo
model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Carregue os arquivos de dados
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))


def preprocess_user_input(user_input):

    bag=[]
    bag_of_words = []

    # tokenize a entrada do usuário
def preprocess_user_input(user_input):
    bow_data_token = nltk.word_tokenize(user_input)
    bow_data_token_2 = get_stem_words(bow_data_token,ignore_words)
    bow_data_token_2 = sorted(list(set(bow_data_token)))

    for word in words: 
        if word in bow_data_token:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)
    bag.append(bag_of_words)
    return np.array(bag)
    
def bot_class_prediction(user_input):
    inp = preprocess_user_input(user_input)
  
    prediction = model.predict(inp)
   
    predicted_class_label = np.argmax(prediction[0])
    
    return predicted_class_label


def bot_response(user_input):

   predicted_class_label =  bot_class_prediction(user_input)
 
   # extraia a classe de predicted_class_label
   predicted_class = "label_data"

   # agora que temos a tag prevista, selecione uma resposta aleatória

   for intent in intents['intents']:
    if intent['tag']==predicted_class:
       
       # selecione uma resposta aleatória do robô
        bot_response = "Ola"
    
        return bot_response
    

print("Oi, eu sou a Estela, como posso ajudar?")

while True:

    # obtenha a entrada do usuário
    user_input = input('Digite sua mensagem aqui: ')
    print("Entrada do Usuário: ",user_input)

    response = bot_response(user_input)
    print("Resposta do Robô: ", response)
