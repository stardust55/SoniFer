#import Chatbot module from chatterbot library 
#import ChatterBotCorpusTrainer from chatterbot.trainers library
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#created ChatBot names Joel
chatbot = ChatBot('Joel')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

print("Hi I am Joel , the Bot ")
print("Your companion in the entire journey")

while True:
     request = input('You: ')
     response = chatbot.get_response(request)
     print('Joel: ', response)



