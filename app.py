#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
from utils import wit_response
import os

app = Flask(__name__)
# ACCESS_TOKEN =  os.environ['SECRET_KEY']
ACCESS_TOKEN = 'EAAQENu0nml0BAA5VZATAIav1GYZBqhQaUwP2gAbybmc4L1mz65fZBZBjzXfx6iHbOtfSTZAVrEDmFuKjLZCGqzdmEmMKPJxqZCMSc7tG2OFFlMVjQ8rBwyZAdFPnSw2ZCgxzCaIuFRs2HYHDhExR3oszDqn4vi80YSle9GTVTN7dW0wZDZD'
				
VERIFY_TOKEN = 'columbia'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST']) #receive, send 
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user\

@app.route("/", methods=['POST'])
def webhook():
	output = request.get_json()
	log(output)
    # get whatever message a user sent the bot
    if output['object'] == 'page':
		for event in output['entry']:
         	messaging = event['messaging']
          	for message in messaging:
            	if message.get('message'):
                	#Facebook Messenger ID for user so we know where to send response back to
	                recipient_id = message['sender']['id']
	                sender_id = message['sender']['id']
	         		if 'text' in message['message']:
						input_text = message['message']['text']
						response_sent_text = get_message(input_text)
						send_message(recipient_id, response_sent_text)
					else:
						input_text = 'no text'
						response_sent_text = get_message(input_text)
						send_message(recipient_id, response_sent_text)
	                # if message['message'].get('text'):
	                #     response_sent_text = get_message()
	                #     send_message(recipient_id, response_sent_text)
	                # #if user sends us a GIF, photo,video, or any other non-text item
	                # if message['message'].get('attachments'):
	                #     response_sent_nontext = get_message(input_text)
	                #     send_message(recipient_id, response_sent_nontext)
 
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message(input_text):
    (entity,value) = wit_response(input_text)
    if value == 'memes':
    	return 'Here is a dank meme /n https://www.facebook.com/groups/1006815496091821/?ref=br_rs'
    else:
    	sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    	return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True)