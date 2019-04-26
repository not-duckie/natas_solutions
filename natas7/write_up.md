# Natas 7
When you see the webpage there nothinh on the page except *Home* and *About*, on click them them nothing happens, but if you see it carefully you observe that the url changes a bit.
## URL
A Uniform Resource Locator, colloquially termed a web address, is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.*

![url-parts](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fqph.fs.quoracdn.net%2Fmain-qimg-942ef9fd07d745fbc4f692c83e2ef496&f=1).

Arguments can be passed to the webpage with the help of **?** parameter. Here in the challenge we see that the url *http://natas7.natas.labs.overthewire.org/index.php?page=home* is showing whatever the is being passed as t argument to the *page* parameter to the url. If not implemented properly this is know as *LFI (Local File Inclucsion)* vulnerability.

So we give it a go and try to print the contents of /etc/passwd to confirm the vlun. we edit the url to be, *http://natas7.natas.labs.overthewire.org/index.php?page=/etc/passwd*.

![1.png](https://github.com/sarthakmisraa/natas_solutions/blob/master/natas7/images/1.png)

we get the contents of the /etc/passwd, it is vlunerable LFI. On examining the source we see that the password is stored in the path */etc/natas_webpass/nata8*, thus we append the url and get our passwd, *http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8*
