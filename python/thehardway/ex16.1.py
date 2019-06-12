from sys import argv
# Filename texteditor.txt
script, filename = argv

print(f"We are going to delete the contents of {filename}")
print(f"If you wish to delete the contents of {filename}, press 'ENTER'")
print("If you wish to cancel, press CTRL + C (^C)")

input("How do you wish to proceed?")
# Opens file for writing using the 'w' as an extra parameter
print("Opening file...")
target = open(filename, 'w')

print("Deleting contents of file...")
print("Content deleted.")

print("Please fill in the file:")
line1 = input(">>> ")
line2 = input(">>> ")
line3 = input(">>> ")
# My solution
target.write(f"{line1}\n{line2}\n{line3}")
# Internet solution
target.write('{}\n{}\n{}\n'.format(line1, line2, line3))
print("New data successfully saved!")
input("Press <enter> to read contents of the new file.")
with open(filename) as f:  
    output = f.read()
target = open(filename)
print(target.read())
input("Press <enter> to close the file.")
target.close()