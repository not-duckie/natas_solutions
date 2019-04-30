# Natas10
Natas level 10 starts similar to the previous level, it prompts us with *Find words containing:* but we notice a new statement here*For security reasons, we now filter on certain characters*, lets view the source code:
```
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```
Now a new filter has been added, but the character we used in previous challenges are not being filter, so lets us try the same injection.
```
"^" /etc/natas_webpass/natas10 #
```
we get the password, i guess there was a simpler solution the previous challenge that we did'nt see.
