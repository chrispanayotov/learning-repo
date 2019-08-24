<?php

require 'functions.php';

class Task {
	public $description;
	public $completed = false;

	public function __construct($description)
	{
		$this->description = $description;
	}

	public function complete()
	{
		$this->completed = true;
	}

	public function isComplete() 
	{
		return $this->completed;
	}
}


$tasks = [
	new Task('Learn PHP'),

	new Task('Make a SQL query'),

	new Task('Create a class')

];

$tasks[1]->complete();

// clean_output($tasks);

require 'index.view.php';

