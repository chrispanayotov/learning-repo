<?php
$input = isset($_POST['input']) ? $_POST['input'] : '';

$asd = str_split($dna);
$qwe = '';

foreach ($asd as $letter) {
	if ($letter == "A") {
		$qwe .= "T";
	} elseif ($letter == "T") {
		$qwe .= "A";
	} elseif ($letter == "C") {
		$qwe .= "G";
	} elseif ($letter == "G") {
		$qwe .= "C";
	}
}

var_dump(($qwe));