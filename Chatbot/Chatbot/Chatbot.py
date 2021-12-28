#import Chatbot module from chatterbot library 
#import ChatterBotCorpusTrainer from chatterbot.trainers library
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json

data = json.loads(open('nfL6.json', 'r').read())

train = []

for k, row in enumerate(data):
    train.append(row['question'])
    train.append(row['answer'])

#created ChatBot names Joel
chatbot = ChatBot('Joel')

trainer1 = ChatterBotCorpusTrainer(chatbot)
trainer1.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)


trainer = ListTrainer(chatbot)

trainer.train(train[:1024])

print("Hi I am Joel , the Bot ")
print("Your companion in the entire journey")

while True:
     request = input('You: ')
     response = chatbot.get_response(request)
     print('Joel: ', response)


