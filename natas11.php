<?php

function xor_encrypt($in) {
    
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    echo $outText;
}


$data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSQwh+REIKaAw=" ;
$tempdata = xor_encrypt(base64_decode($data));
//echo $tempdata;
//tempdata = json_decode( xor_encrypt (base64_decode ($data]) ) , true);
echo $tempdata ;

?>