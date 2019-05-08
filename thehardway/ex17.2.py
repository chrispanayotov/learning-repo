from sys import argv
# from_file = ex17.txt, to_file = new_file.txt

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())


