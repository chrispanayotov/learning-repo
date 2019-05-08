from sys import argv
from os.path import exists
# from_file is ex17.txt, to_file is new_file.txt
script, from_file, to_file = argv

indata = open(from_file).read()
print(f"Copying data from {from_file} to {to_file}...")
print(f"Does the output file exist? {exists(to_file)}")
print(f"Length of file is {len(indata)} bytes")
open(to_file, 'w').write(indata)

print("All done.")