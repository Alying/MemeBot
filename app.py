#Python libraries that we need to import for our bot
import random
from flask import Flask, request, render_template
from pymessenger.bot import Bot
from utils import wit_response
from meme_sifter import meme_getter
from automate import sendMessage, regMessage, scheduleMessage
from userMongo import addPersonMongo, updateInfo, delSubs, returnInfo
import os, sys

app = Flask(__name__)
# ACCESS_TOKEN =  os.environ['SECRET_KEY']
ACCESS_TOKEN = 'EAAQENu0nml0BAA5VZATAIav1GYZBqhQaUwP2gAbybmc4L1mz65fZBZBjzXfx6iHbOtfSTZAVrEDmFuKjLZCGqzdmEmMKPJxqZCMSc7tG2OFFlMVjQ8rBwyZAdFPnSw2ZCgxzCaIuFRs2HYHDhExR3oszDqn4vi80YSle9GTVTN7dW0wZDZD'
VERIFY_TOKEN = 'columbia'
bot = Bot(ACCESS_TOKEN)
# looper = False

@app.route('/')
def index():
	return render_template('index.html', name='MemeBot')

@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						input_text = messaging_event['message']['text']
					else:
						input_text = 'no text'

					# if input_text == 'Subscribe':
					# 	response = "Sure! Your daily subscription will begin. Message stop to stop. "
					# 	bot.send_text_message(sender_id, response)
					# 	memes = meme_getter(10)
					# 	meme = random.choice(memes)
					# 	bot.send_text_message(sender_id, meme)
					# 	looper = True
					# 	regMessage(memes,10)
						 
					# elif input_text == 'Stop':
					# 	looper = False

					response = get_message(input_text)
					bot.send_text_message(sender_id, response)

	return "ok", 200

# def check(): 
# 	return looper 

def log(message):
	print(message)
	sys.stdout.flush()

def get_message(input_text):
	value = wit_response(input_text)
	if value == 'memes':
		memes = meme_getter(5)
		meme = random.choice(memes)
		return 'Here is a dank meme {}'.format(meme)
	else:
		sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
		return random.choice(sample_responses)

if __name__ == "__main__":
	app.run(debug = True, port = 80)