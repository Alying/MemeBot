import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/331078540726047"
f = "fields=posts.limit(2){likes.summary(true),link,picture}"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{f}&{params}".format(host=host, path=path, f=f, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype (dictionary)
me = json.loads(resp)

#me is a dictionary, me.keys() is a list, me.values() is a list
print(type(me))
print(me.keys())
print(type(me.keys()))
print(me.values())
print(type(me.values()))

# display the result
pprint.pprint(me)

def meme_getter(num_of_posts):
	li = []

	# of the two keys in the dictionary, the first is the posts; the second is the user id
	posts, paging, user_id = me.keys()

	#image url
	for i in range(num_of_posts)
		meme_url =  me[posts][data][i]["link"]
		picture_preview = me[posts][data][i]["pic"]
		full_meme_package = [meme_url, picture_preview]
		li.extend(full_meme_package)

	return li