import os, sys
import json
import urllib
import pprint
import pkgs.facebookinsights.commands as commands

# get Facebook access token from environment variable
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/me"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{params}".format(host=host, path=path, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
me = json.loads(resp)

# display the result
pprint.pprint(me)

#pprint,pprint(graph.get_object('me'))


#def get_page_memes (page):
#	page_ID = fi.authenticate()
#	print(page_ID)