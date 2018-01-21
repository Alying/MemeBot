#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
from utils import wit_response
from meme_sifter import meme_getter
import os, sys

app = Flask(__name__)
# ACCESS_TOKEN =  os.environ['SECRET_KEY']
ACCESS_TOKEN = 'EAAQENu0nml0BAA5VZATAIav1GYZBqhQaUwP2gAbybmc4L1mz65fZBZBjzXfx6iHbOtfSTZAVrEDmFuKjLZCGqzdmEmMKPJxqZCMSc7tG2OFFlMVjQ8rBwyZAdFPnSw2ZCgxzCaIuFRs2HYHDhExR3oszDqn4vi80YSle9GTVTN7dW0wZDZD'
VERIFY_TOKEN = 'columbia'
bot = Bot(ACCESS_TOKEN)

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
				x = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					response = get_message(messaging_text)
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()

def get_message(input_text):
    value = wit_response(input_text)
    if value == 'memes':
    	meme = meme_getter(2)
    	meme = meme[0:2]
    	return 'Here is a dank meme {}'.format(meme)
    else:
    	sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    	return random.choice(sample_responses)

if __name__ == "__main__":
	app.run(debug = True, port = 80)

