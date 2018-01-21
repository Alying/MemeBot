from time import sleep
from datetime import datetime, timedelta
from threading import Timer

def sendMessage(message):
	print(message)

def regMessage(message, hour):
	x = datetime.today()
	y = x.replace(day=x.day+1, hour = 8, minute=0, second=0, microsecond=0)
	delta_t = y - x

	

def scheduleMessage(daysOfWeek, message):
	now = datetime.now()
	runat = now + timedelta(seconds = 15)
	delay = (runat - now).total_seconds()
	Timer(delay, sendMessage, [message]).start()

scheduleMessage(3, 'hi')
sleep(3);
scheduleMessage(3, 'hey')