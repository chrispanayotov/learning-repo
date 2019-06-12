# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them 
# the year that they will turn 100 years old.
from datetime import date
import os
name = input("What is your name? ")
age = int(input("How old are you? "))

current_year = date.today().year
hundred_years = 100 - age 
# Internet Solution
#hundred_years = str((2019 - age)+100)
print("Hey {}!".format(name))
print("You are {} years old!".format(age))
print("You will become 100 years old in the year {}.".format(hundred_years))
future_year = current_year + hundred_years
print("That will be the year {}!".format(future_year))
