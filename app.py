#Python libraries that we need to import for our bot
import random
from flask import Flask, request, render_template
from pymessenger.bot import Bot
from utils import wit_response
from meme_sifter import meme_getter
import fbmq
from automate import sendMessage, regMessage, scheduleMessage
from userMongo import addPersonMongo, updateInfo, delSubs, returnInfo
import os, sys
import config

app = Flask(__name__)
# ACCESS_TOKEN =  os.environ['SECRET_KEY']
#FB Messenger Token
ACCESS_TOKEN = config.ACCESS_TOKEN
VERIFY_TOKEN = config.VERIFY_TOKEN
bot = Bot(ACCESS_TOKEN)
#looper = False

#messenger introduction
page = fbmq.Page(ACCESS_TOKEN,api_ver="v2.11")
page.greeting("Welcome to MemeBot! Chat with us to get memes or compliments.")

@app.route('/')
def index():
	return render_template('index.html', name='MemeBot')

#receiving messages
@app.route('/', methods=['GET']) 
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

#sending messages
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

					'''if input_text == 'Subscribe':
						response = "Sure! Your daily subscription will begin. Message stop to stop. "
						bot.send_text_message(sender_id, response)
						memes = meme_getter(10)
						meme = random.choice(memes)
						bot.send_text_message(sender_id, meme)
						looper = True
						regMessage(memes,10)
						 
					elif input_text == 'Stop':
						looper = False
					else:'''
					response = get_message(input_text)
					bot.send_text_message(sender_id, response)

	return "ok", 200

# def check(): 
# 	return looper 

def log(message):
	print(message)
	sys.stdout.flush()

def get_message(input_text):
	value = wit_response(input_text) #value is the value WIT.AI returns
	if input_text == 'bird meme':
		return 'Here is bird meme! https://www.facebook.com/331078540726047/photos/a.331493887351179.1073741827.331078540726047/331643797336188/?type=3&theater'
	elif value == 'memes':
		memes = meme_getter(5)
		meme = random.choice(memes)
		return 'Here is a nice meme! {}'.format(meme)
	else:
		sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're grateful to know you :)",
		 "Your smile is contagious.", "You're a smart cookie.", "Is that your picture next to 'charming' in the dictionary?"]
    # return selected item to the user
		return random.choice(sample_responses)

if __name__ == "__main__":
	app.run(debug = True, port = 80)


def sendMessage(messages, period):
	message = random.choice(messages)
	#change message and boolean here

	bot.send_text_message(message)

	if looper:
		regMessage(messages, period)

def regMessage(messages, period): #period in seconds
	x = datetime.now()
	runat = now + timedelta(seconds = period)

	delay = (runat - now).total_seconds()

	Timer(delay, sendMessage, [messages, period]).start()