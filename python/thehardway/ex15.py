# imports the argument variables module/library
from sys import argv
# Define variables for argv, filename is ex15_sample.txt
script, filename = argv
# define var txt to function open to pull argument variable filename
txt = open(filename)
# Read and print the contents of the txt file
print(f"Here's your file {filename}:")
print(txt.read())
# Close the opened txt file
txt.close()
# Prompts the user to write the name of the file again
print("Type the filename again:")
file_again = input("> ")
# Opens the file again
txt_again = open(file_again)
# Reads and prints the contents of the txt file again
print(txt_again.read())
# Close the reopened txt file
txt_again.close()
