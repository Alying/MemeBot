import sys
import pymongo

uri = 'mongodb://person1:person1@ds263837.mlab.com:63837/memebot' 

###############################################################################
# main
###############################################################################

client = pymongo.MongoClient(uri)
db = client.get_default_database()
people = db.people

def addPersonMongo(name):
	person = {'user':name,
	'memeType':None,
	'time': None
	}

	people.insert_one(person)

def updateInfo(name, memeType, time):
	people.update_one(
	{'user':name},
	{'$set':{'memeType':memeType, 'time':time},
	'$currentDate':{'lastModified':True}}
	)

def delSubs(name):
	db.people.delete_many({'user':name})

def returnInfo(name):
	print(people.find_one({'user':name}))