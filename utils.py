from wit import Wit 

access_token = 'ECYGVCSYYK7NGSNAF55QVL5DRD6VM7IH'
client = Wit(access_token)

def wit_response(message):
	resp = client.message(message, verbose = True)
	entity = None
	value = None

	try: 
		entity = list(resp['entities'])[0]
		value = resp['entities'][str(entity)][0]['value']
	except: 
		pass
	return entity, value

entity, value = wit_response('send memes')
print(entity)
print(value)