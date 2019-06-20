import sys
a = int(input())
b = int(input())
max_passwords = int(input())

A_ascii = 35
B_ascii = 64
generated_passes = 0

while True:
    for num_x in range(1, a + 1):
        for num_y in range(1, b + 1):
            if generated_passes < max_passwords:
                print(f"{chr(A_ascii)}{chr(B_ascii)}{num_x}{num_y}{chr(B_ascii)}{chr(A_ascii)}", end='|')
                
                A_ascii += 1
                B_ascii += 1
                generated_passes += 1

                if A_ascii > 55:
                    A_ascii = 35
                if B_ascii > 96:
                    B_ascii = 64
            else:
                sys.exit()
    break