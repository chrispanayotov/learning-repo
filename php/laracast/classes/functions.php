<?php

function clean_output($output) {
	echo "<pre>";

	die(var_dump($output));

	echo "</pre>";
}