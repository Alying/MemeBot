import sys
import pymongo

uri = 'mongodb://person1:person1@ds263837.mlab.com:63837/memebot' 

###############################################################################
# main
###############################################################################

client = pymongo.MongoClient(uri)
db = client.get_default_database()
posts = db.posts

def addPersonMongo(name):
	person = {'user':'name',
	'memeType':None,
	'time': None
	}

