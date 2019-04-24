# Natas 4
The prompt here says *Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"*
This means all we have to do in order to gain access is add a header to the request. It can be achieved by capturing the request with burpe and editing the header or we can use the python script.
I have written a python script for it.