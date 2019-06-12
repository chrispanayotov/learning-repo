# Import module argument var from sys
from sys import argv
# filename texteditor.txt
script, filename = argv
# Prompts the user to choose if he wants to delete content of filename or cancel
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("How do you want to proceed?")
# Opens filename and deletes it's contents
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
print(input("Press <enter>  to continue"))

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("File overwritten... closing.")
print("File closed.")
target.close()
