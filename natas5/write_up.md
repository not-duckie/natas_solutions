# Natas 5
We get a prompt that says *Access disallowed. You are not logged in*, to further investigate we could either user burpe to intercept the request and analyze it but we are using python for all the solutions so we inspect element to see the sent out requests and then a write suitable python requests.
1. Press *Ctrl+Shift+i* to open developer tools and click on *Networking* tab and then click on *ALL* (exactly below the network tab) to see all the requests.
1. Click on the request to select the GET request and then on right side click on *headers* tab.
1. On analyzing the headers we see a weird set-cookie *loggedin=0*, the set-cookie is the header in the response tag saying to set the cookie to this so the server could identify us as not logged in.
1. But we are hackerman :P we will do somewhat opposite of that, we will add that cookie but set it value to 1 or any other number other than zero
1. I have written a python script for it. 