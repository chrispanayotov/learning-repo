from sys import argv
from os.path import exists
# from_file is test.txt to_file is new_file.txt
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

#Internet solution
#with open(from_file) as in_file, open(to_file, 'w') as out_file:
#    indata = in_file.read()
#    out_file.write(indata)
