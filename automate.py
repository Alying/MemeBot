from time import sleep
import random
from datetime import datetime, timedelta
from threading import Timer

def sendMessage(messages, period, repeat):
	print(random.choice(messages))
	#change message and boolean here

	repeat = check()
	regMessage(message, period, repeat)

def regMessage(messages, period, repeat): #period in seconds
	x = datetime.today()
	ymin, ysec, yhour= 0,0,x.hour

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
	delta_t = y - x

	delay = delta_t.total_seconds()

	Timer(delay, sendMessage, [messages, period, repeat]).start()

def scheduleMessage(daysOfWeek, message):
	now = datetime.now()
	runat = now + timedelta(seconds = 15)
	delay = (runat - now).total_seconds()
	Timer(delay, sendMessage, [message]).start()

'''
scheduleMessage(3, 'hi')
sleep(3);
scheduleMessage(3, 'hey')

regMessage('sup', 3)'''