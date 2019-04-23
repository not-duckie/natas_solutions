import requests
#to make a google search with python will require a extra python module.
# therefore in order to keep this light, this is direclty making request to link
url = 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'
user = 'natas3'
passw = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
print ((requests.get(url,auth=(user,passw))).text)