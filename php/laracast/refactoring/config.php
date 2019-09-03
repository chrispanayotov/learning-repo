<?php

return [
	'database' => [
		'name' => 'todo',
		'username' => 'root',
		'password' => 'Serial Qiller Lynching',
		'connection' => 'mysql:host=127.0.0.1',
		'options' => [
			PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
		]
	]
];