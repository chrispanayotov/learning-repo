from sys import argv
# filename is sample.txt
script, filename = argv
txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.readline())
txt.close()
