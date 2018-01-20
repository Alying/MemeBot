import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/331078540726047"
f = "fields=posts.limit(5){likes.summary(true),link,picture}"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{f}&{params}".format(host=host, path=path, f=f, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
me = json.loads(resp)

# display the result
pprint.pprint(me)