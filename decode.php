<?php

function xor_encrypt($in) {
    
   // $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $key = base64_decode("cXc4SnF3OEpxdzhKcXc4SnF3OEpxdzhKcXc4SnF3OEpxJW4YIiRsSnE=");
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


$data = array("showpassword"=>"yes", "bgcolor"=>"#ffffff") ;
$tempdata = base64_encode(xor_encrypt(json_encode($data)));
//echo $tempdata;
//tempdata = json_decode( xor_encrypt (base64_decode ($data]) ) , true);
echo $tempdata;

?>