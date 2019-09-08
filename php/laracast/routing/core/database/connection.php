<?php

class Connection 
{
	// Static makes a method globally accessible, without requiring an instance
	public static function make($config) 
	{
		try {
			return new PDO(
				$config['connection'].';dbname='.$config['name'],
				$config['username'],
				$config['password'],
				$config['options']
			);

		} catch (PDOException $ex) {
			die($ex->getMessage());
		}
	}
}