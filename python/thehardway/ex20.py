# Import argument var module from sys
from sys import argv
# Set arguments, input_file = test.txt
script, input_file = argv
# Define function print_all with argument f to read the input_file (test.txt)
def print_all(f):
    print(f.read())
# Define function rewind with argument f that ->
# -> returns at the offset of the test.txt file
def rewind(f):
    f.seek(0)
# Define function print a line with arguments line_count and f ->
# -> to print and read a line
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Define var to open the input file (test.txt)
current_file = open(input_file)
# Prints the whole content of test.txt by calling print_all funcition
print("First let's print the whole file: \n")

print_all(current_file)
# Calls function rewind to return the position of the file to the beginning
print("Now let's rewind the file, just like a tape")
rewind(current_file)

print("Let's print three lines:")
# Calls function print_a_line to print text on three diferrent lines
current_line = 1
print_a_line(current_line, current_file) # Line 1

current_line += current_line 
print_a_line(current_line, current_file) # Line 2

current_line += current_line 
print_a_line(current_line - 1, current_file) # Line 3