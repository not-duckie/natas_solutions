import requests
import re

url = 'http://natas0.natas.labs.overthewire.org/'
#credentials for connection
user = 'natas0'
passw = 'natas0'
session = requests.session()
r = session.get(url,auth=(user,passw))
a = r.text
for i in a.splitlines():
	if "natas1" in  i:
		print i