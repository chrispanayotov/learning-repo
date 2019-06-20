n = input()

ascii_symb = 0

for i in range(len(n), 0, -1):
    i = int(n[i-1])
    
    if i == 0:
        print("ZERO")
    else:
        ascii_symb = i + 33
        print(chr(ascii_symb) * i)