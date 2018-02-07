from time import sleep
import random
from datetime import datetime, timedelta
from threading import Timer
# from app import check
from pymessenger.bot import Bot
import config
import os

ACCESS_TOKEN =  os.environ['ACCESS_TOKEN']
bot = Bot(ACCESS_TOKEN)

def sendMessage(messages, period):
	message = random.choice(messages)
	#change message and boolean here

	bot.send_text_message(message)

	if check() == True:
		regMessage(messages, period)

def regMessage(messages, period): #period in seconds
	x = datetime.now()
	runat = now + timedelta(seconds = period)
	'''ymin, ysec, yhour= 0,0,x.hour

	if (x.second + period > 59):
		if x.minute == 59:
			ymin = 0
			yhour += 1
		else:
			ymin = x.minute + 1
		ysec = (x.second + period) % 60
	else:
		ymin = x.minute
		ysec = x.second + period

	y = x.replace(day=x.day, hour = yhour, minute=ymin, second=ysec, microsecond=0)
	delta_t = y - x'''

	delay = (runat - now).total_seconds()

	Timer(delay, sendMessage, [messages, period]).start()

def scheduleMessage(daysOfWeek, message):
	now = datetime.now()
	runat = now + timedelta(seconds = 15)
	delay = (runat - now).total_seconds()
	#Timer(delay, sendMessage, [message]).start()

'''
scheduleMessage(3, 'hi')
sleep(3);
scheduleMessage(3, 'hey')

regMessage('sup', 3)'''