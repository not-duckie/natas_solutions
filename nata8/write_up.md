# Natas 8
In this level similar to previous level we get to enter a password which will be checked by the server and on the basis of which it will permit the entry. When we view the source code we get:
`<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>`
The php code takes the user submitted string encode it, and if it matches the *$enocdedSecret* , we will get the password for next  level.
So lets decode the *$enocdedSecret*, we will do exactly the reverse of `bin2hex(strrev(base64_encode($secret)))`. I'll will use php to decode it in order to solve this.
1. we will be doing exact reverse of the mentioned function in php
`<?php
$nice = '3d3d516343746d4d6d6c315669563362';
echo base64_encode(strrev(hex2bin('$nice')));
?>` 
