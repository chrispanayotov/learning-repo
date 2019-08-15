<?php

$input = isset($_POST['input']) ? $_POST['input'] : '';

$multilineInput = explode("\r\n", $input);

$output = '';
$numbers = str_split($input);

foreach ($numbers as $num) {
	$output .= (int)$num * (int)$num;
}

var_dump($output);

var_dump($multilineInput);

var_dump($input);