<?php

require '../functions.php';

require 'task.php';


$pdo = connectToDb();

$statement = $pdo->prepare('select * from mytodos');

$statement->execute();

$tasks = $statement->fetchAll(PDO::FETCH_CLASS, 'Task');


require 'index.view.php';