# Natas 6
The Page has a *Input secret* field, we see the source code for the form enumerations,

`<?
include "includes/secret.inc";
    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>`

It takes the value of variable secret via a POST request i.e *$_POST['secret'])* and prints the password for the next level if it matches the variale $secret.

So we go to *include/secret.inc* to see what is the value of variable *$secret*. When we open the *http://natas6.natas.labs.overthewire.org/includes/secret.inc* page we see blank page, so we press *Ctrl+U* to view the page source and we see the value of $secret i.e **FOEIUWGHFEEUHOFUOIU**.
So we enter the value and get the password for the next level. 