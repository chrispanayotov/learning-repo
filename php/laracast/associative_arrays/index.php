<?php

$person = [
	'age' => 31,
	'hair' => 'brown',
	'color' => 'purple'
];

$person['name'] = 'Chris';
unset($person['age']);

echo '<pre>';
die(var_dump($person));
echo '</pre>';

require 'index.view.php';