from sys import argv; scpt, fr, to = argv; open(to, 'w').write(open(fr).read())
with open("ex17.txt") as fr:
    from_file = fr.read()