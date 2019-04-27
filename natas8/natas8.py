import requests
import subprocess
import os

url = 'http://natas8.natas.labs.overthewire.org/'
user = 'natas8'
passw = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
data = { 'secret': 'oubWYf2kBq',
		'submit' : 'Submit Query' }
r1 = requests.post(url,data=data,auth=(user, passw))

for i in (r1.text).splitlines():
	if "password" in i:
		print i
