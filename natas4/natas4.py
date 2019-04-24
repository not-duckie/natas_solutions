import requests

url = 'http://natas4.natas.labs.overthewire.org/'
user = 'natas4'
passw = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
headers = {'referer':'http://natas5.natas.labs.overthewire.org/'}
r = requests.get(url, headers=headers, auth=(user,passw))
a = r.text
for i in a.splitlines():
	if 'natas5' in i:
		print i