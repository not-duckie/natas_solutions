import requests
import re

url = 'http://natas0.natas.labs.overthewire.org/'
#credentials for connection
user = 'natas0'
passw = 'natas0'
session = requests.session()
r = session.get(url,auth=(user,passw))
#this is to match <!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
# password = (re.search('is*', r.text)).group(1)
print (r.text)