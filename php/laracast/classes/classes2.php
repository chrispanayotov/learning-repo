<?php

interface UniversityMember
{
	private $position;
	private $title;

	public function goToUniversity();
}


class Human
{
    private $age;
    private $name;

    public function __construct($age, $name)
    {
        $this->setAge($age);
        $this->setName($name);
    }

	public function setAge($age)
	{
		$this->age = $age;

		return $this;
	}

	public function getAge()
	{
		return $this->age;
	}

	public function setName($name)
	{
		$this->name = $name;

		return $this;
	}

	public function getName()
	{
		return $this->name;
	}
}


class Student extends Human implements UniversityMember
{
    private $specialty;
    private $facultyNumber;
	private $position;
	private $title;

    public function __construct($age, $name, $specialty, $facultyNumber)
    {
        $this->setSpecialty($specialty);
        $this->setFacultyNumber($facultyNumber);
		  $this->position = 'Student';
		  $this->title = 'N/A';

        parent::__construct($age, $name);
    }

	public function setSpecialty($specialty)
	{
		$this->specialty = $specialty;

		return $this;
	}

	public function getSpecialty()
	{
		return $this->specialty;
	}

	public function setFacultyNumber($facultyNumber)
	{
		$this->facultyNumber = $facultyNumber;

		return $this;
	}

	public function getFacultyNumber()
	{
		return $this->facultyNumber;
	}

	public function goToUniversity()
	{
		// go to lectures
	}
}


class Professor extends Human implements UniversityMember
{
	 private $position;
	 private $title;

    public function __construct($age, $name)
    {
		  $this->position = 'Teacher';
		  $this->title = 'Professor';

        parent::__construct($age, $name);
    }

	public function goToUniversity()
	{
		// go to work
	}
}