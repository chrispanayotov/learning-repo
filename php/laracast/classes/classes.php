<?php

class Human
{
    private $age;
    private $name;

    public function __construct($age, $name)
    {
        if (is_int($age) == false) {
			throw new Exception('Age provided must be of type INT');
		} else {
			$this->setAge($age);
		}
        $this->setName($name);
    }
}

class Student extends Human
{
    private $specialty;
    private $facultyNumber;

    public function __construct($age, $name, $specialty, $facultyNumber)
    {
        $this->setSpecialty($specialty);
        $this->setFacultyNumber($facultyNumber);

        parent::__construct($age, $name);
    }
}

$student = new Student(15, 'Chris', 'Psychology', 'f60000');