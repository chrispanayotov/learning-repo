<?php

$query = require 'bootstrap.php';
require '../pdo/task.php';


$tasks = $query->selectAllFromTable('mytodos', 'Task');

require 'index.view.php';