import sys
n = int(input())

evenSum = 0
oddSum = 0
evenMax = -sys.maxsize-1
oddMax = -sys.maxsize-1
evenMin = sys.maxsize
oddMin = sys.maxsize

for num in range(1, n + 1):
    current_num = float(input())
    if num % 2 == 0: # If check for an even iteration
        evenSum += current_num
        if current_num > evenMax: # Get the max even number
            evenMax = current_num
        if current_num < evenMin: # Get the min even number
            evenMin = current_num
    elif num % 2 != 0: # If check for an odd iteration
        oddSum += current_num
        if current_num > oddMax: # Get the max odd number
            oddMax = current_num
        if current_num < oddMin: # Get the min odd number
            oddMin = current_num

if oddSum != 0:
    print(f"OddSum={oddSum:.2f},")
    print(f"OddMin={oddMin:.2f},")
    print(f"OddMax={oddMax:.2f},")
else:
    print(f"OddSum={oddSum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")
if evenSum != 0:
    print(f"EvenSum={evenSum:.2f},")
    print(f"EvenMin={evenMin:.2f},")
    print(f"EvenMax={evenMax:.2f}")
else:
    print(f"EvenSum={evenSum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")