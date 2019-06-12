import sys
n = int(input())

counter = 0

while counter < n:
    for i in range(66, 77, 2):
        for j in range(102, 96, -1):
            for k in range(65, 68):
                for l in range(1, 11):
                    for p in range(10, 0, -1):
                        counter += 1
                        if counter == n:
                            print(f"Ticket combination: {chr(i)}{chr(j)}{chr(k)}{l}{p}")
                            print(f"Prize: {i + j + k + l + p} lv.")