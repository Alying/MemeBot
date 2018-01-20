from time import sleep
from datetime import datetime, timedelta
from threading import Timer

def sendMessage(message):
	print(message)

def scheduleMessage(daysOfWeek, message):
	now = datetime.now()
	runat = now + timedelta(seconds = 15)
	delay = (runat - now).total_seconds()

	print runat
	print delay

	Timer(delay, sendMessage, [message]).start()

scheduleMessage(3, 'hi')
sleep(3);
scheduleMessage(3, 'hey')