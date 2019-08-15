<?php
$input = isset($_POST['input']) ? $_POST['input'] : '';

$letters = explode(', ', $input);
$numbers = [];
  
  foreach ($letters as $letter) {
    $numbers[] = ord($letter);
  }
  
  $asd = range(min($numbers), max($numbers));
  $missing = chr(array_values(array_diff($asd, $numbers))[0]);


var_dump($missing);