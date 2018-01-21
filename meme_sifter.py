import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
ACCESS_TOKEN = 'EAACEdEose0cBAFRwHXfQsABqBJD5yWzNnfaCv712wBWtnFngcOemH7sf2oh8pbgiwyG6WdMmjGZAD2Li9kYyV8ZC4A1MYOy27S3hKjVkPjMuKE6nvkRxc71mp3cGq9BGh7ZBp5X5Ld7tuYgAkf5gfDqKA12ZA68rJjcL6ZBCQfZAGuE9H64r5ZBoEvd9WsBSjINP6zbcrs4HQZDZD'

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/331078540726047"
f = "fields=posts{likes.summary(true),link,picture}"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{f}&{params}".format(host=host, path=path, f=f, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype (dictionary)
me = json.loads(resp)

#me is a dictionary, me.keys() is a list, me.values() is a list

# display the result
#pprint.pprint(me)

#num_of_posts = number of posts, in most-recent to least-recent order
def meme_getter(num_of_posts):
	try:
		li = []

		# of the two keys in the dictionary, the first is the posts; the second is the user id
		(posts, user_id) =  me.keys()

		for i in range(num_of_posts):
 			meme_url =  me[posts]["data"][i]["link"]
 			print meme_url
 			#likes_summary = me[posts]["data"][i]["likes"][2]
 			#total_count = likes_summary[summary][total_count]

 			#print(meme_url)
 			#picture_preview = me[posts]["data"][i]["picture"]
 			#print(picture_preview)
 			#full_meme_package = [meme_url, picture_preview]
 			li.append(meme_url)
	
		return li
	except IndexError:
		print("There are not enough memes posted in the group yet :(")
