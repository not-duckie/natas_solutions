import requests

url = 'http://natas20.natas.labs.overthewire.org/index-source.html'
username = 'natas20'
passw = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

r = requests.get(url,auth=(username,passw))

response = r.text

print response
