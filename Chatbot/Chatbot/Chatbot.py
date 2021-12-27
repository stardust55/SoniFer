from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer



chatbot = ChatBot('Joel')

trainer = ChatterBotChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

while True:
     request = input('You: ')
     response = chatbot.get_response(request)
     print('Bot: ', response)


