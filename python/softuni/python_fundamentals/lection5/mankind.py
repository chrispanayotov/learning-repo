class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}"
    

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if not value.istitle():
            raise Exception(f"Expected upper case letter! Argument: firstName")
        if len(value) < 4:
            raise Exception(f"Expected length at least 4 symbols! Argument: firstName")
        self.__first_name = value
    

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        if not value.istitle():
            raise Exception(f"Expected upper case letter! Argument: lastName")
        if len(value) < 3:
            raise Exception(f"Expected length at least 3 symbols! Argument: lastName")
        self.__last_name = value


class Student(Human):
    def __init__(self, first_name, last_name, faculty_num):
        super().__init__(first_name, last_name)
        self.faculty_num = faculty_num

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_num}"
    

    @property
    def faculty_num(self):
        return self.__faculty_num
    
    @faculty_num.setter
    def faculty_num(self, value):
        if not 5 <= len(value) <= 10:
            raise Exception("Invalid faculty number!")
        for char in value:
            if char.isdigit() == False and char.isalpha() == False:
                raise Exception("Invalid faculty number!")
        self.__faculty_num = value    


class Worker(Human):
    def __init__(self, first_name, last_name, week_salary, hours_per_day):
        super().__init__(first_name, last_name)
        self.week_salary = week_salary
        self.hours_per_day = hours_per_day
        self.salary_per_hour = (self.week_salary / self.hours_per_day) / 5

    def __str__(self):
        return f"""
                First Name: {self.first_name}\nLast Name: {self.last_name}
                Week Salary: {self.week_salary:.2f}
                Hours per day: {self.hours_per_day:.2f}
                Salary per hour: {self.salary_per_hour:.2f}""".lstrip()
    

    @property
    def week_salary(self):
        return self.__week_salary
    
    @week_salary.setter
    def week_salary(self, value):
        if value < 10:
            raise Exception(f"Expected value mismatch! Argument: weekSalary")
        self.__week_salary = value
    

    @property
    def hours_per_day(self):
        return self.__hours_per_day
    
    @hours_per_day.setter
    def hours_per_day(self, value):
        if not 1 <= value <= 12:
            raise Exception(f"Expected value mismatch! Argument: workHoursPerDay")
        self.__hours_per_day = value

first_name, last_name, faculty_num = input().split()
worker_first, worker_last, salary, hours = input().split()

try:
    student = Student(first_name, last_name, faculty_num)
    worker = Worker(worker_first, worker_last, float(salary), float(hours))
    print(student)
    print()
    print(worker)
except Exception as f:
    print(f)