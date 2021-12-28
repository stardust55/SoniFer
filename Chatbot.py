# import Chatbot module from chatterbot library
# import ChatterBotCorpusTrainer from chatterbot.trainers library
# import ListTrainer from chatterbot.trainers library
# importing json file
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json

data = json.loads(open('nfL6.json', 'r').read())

train = []

for k, row in enumerate(data):
    train.append(row['question'])
    train.append(row['answer'])

# created ChatBot named Trevor
chatbot = ChatBot('Trevor')


def train_bot():
    trainer1 = ChatterBotCorpusTrainer(chatbot)
    trainer1.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations"
    )

    trainer = ListTrainer(chatbot)

    # Training the Bot
    # Limiting the questions and answers database to 1024 as it
    # would take time in loading
    trainer.train(train[:1024])


def get_bot_response(text):
    return chatbot.get_response(text)


if __name__ == '__main__':
    print("Hi I am Trevor, the Bot ")
    print("Your companion in the entire journey")

    while True:
        request = input('You: ')
        response = chatbot.get_response(request)
        print('Trevor: ', response)
