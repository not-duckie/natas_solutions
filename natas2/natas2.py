import requests

url = 'http://natas2.natas.labs.overthewire.org/files/users.txt'
user = 'natas2'
passw = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

r = requests.get(url,auth=(user,passw))
print (r.text)