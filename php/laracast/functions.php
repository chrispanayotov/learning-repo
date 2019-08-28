<?php

function clean_output($output) {
	echo "<pre>";

	var_dump($output);

	echo "</pre>";
}

function connectToDb(){
	try {
		return new PDO('mysql:host=127.0.0.1;dbname=todo', 'root', '');
	} catch (PDOException $e) {
		$e->getMessage();
	}
}