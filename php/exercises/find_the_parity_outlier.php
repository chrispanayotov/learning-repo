<?php
$input = isset($_POST['input']) ? $_POST['input'] : '';

$numbers = explode(', ', $input);

$odd = $even = [];
foreach ($integers as $num) {
	if ($num % 2 != 0) {
		$odd[] = $num;
	} else {
		$even[] = $num;
	}
}

if (count($odd) == 1) {
	return $odd[0];
} elseif (count($even) == 1) {
	return $even[0];
}

var_dump($odd);
var_dump($even);