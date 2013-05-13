import urllib
import json

res = urllib.urlopen("http://search.twitter.com/search.json?q=facebook")
res = json.load(res)
for tweet in res['results']:
  print tweet['text']
  
