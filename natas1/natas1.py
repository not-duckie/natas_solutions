import requests

url = 'http://natas1.natas.labs.overthewire.org'
user = 'natas1'
passw = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

r = requests.get(url,auth=(user,passw))
a = r.text
for i in a.splitlines():
	if "natas2" in i:
		print i