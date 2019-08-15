<?php
$input = isset($_POST['input']) ? $_POST['input'] : '';

$numbers = str_split($input);
$total = 0;
$exp = count($numbers);

foreach ($numbers as $num) {
	$num = pow($num, $exp);
	$total += (int)$num;
}

var_dump($total);