juniors = int(input())
seniors = int(input())
trace = input()

if trace == "trail":
    result = (juniors * 5.50) + (seniors * 7)
elif trace == "cross-country":
    result = (juniors * 8) + (seniors * 9.50)
    if juniors + seniors >= 50:
        result -= result * .25
elif trace == "downhill":
    result = (juniors * 12.25) + (seniors * 13.75)
elif trace == "road":
    result = (juniors * 20) + (seniors * 21.50)

result -= result * .05

print(f"{result:.2f}")