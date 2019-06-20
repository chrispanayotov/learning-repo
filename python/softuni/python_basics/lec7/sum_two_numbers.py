n1 = int(input())
n2 = int(input())
magic_num = int(input())

combinations = 0
is_magic = False

for i in range(n1, n2+1):
    for j in range(n1, n2+1):
        combinations += 1
        
        if i + j == magic_num:
            print(f"Combination N:{combinations} ({i} + {j} = {magic_num})")
            is_magic = True

    if is_magic == True:
        break

if is_magic == False:
    print(f"{combinations} combinations - neither equals {magic_num}")