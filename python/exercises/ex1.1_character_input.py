from datetime import date

def main():
    name = get_name()
    age = get_age()
    bday_yet = birthday_yet()
    year = get_year(int(age), bday_yet)

    if year == 'greater':
        print("You're already 100 years old or greater!")
    else:
        print("Hello, {}!". format(name))
        print("You will turn 100 in the year {}.".format(year))

def get_name():
    return (input("Please enter your name: "))

def get_age():
    return (input("Please enter your age: "))

def birthday_yet():
    answer = input("Have you had your birthday this year yet (y/n)? ")
    if 'y' in answer.lower():
        return True
    else:
        return False

def get_year(a, b):
    assert a >= 0, "Age is not allowed to be less than zero."
    if a >= 100:
        return 'greater'
    else:
        today = str(date.today()).split('-')
        if bool(b) == True:
            this_year = int(today[0])
            return (this_year + (100 - a))
        else:
            this_year = int(today[0])
            return (this_year + (99 - a))

if __name__ == "__main__":
    main()
