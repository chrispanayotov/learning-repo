def sum_even(num):
    x = 0
    for i in range(len(num)):
        y = int(num[i])
        if y % 2 == 0:
            x += y
    return x


def sum_odd(num):
    x = 0
    for i in range(len(num)):
        y = int(num[i])
        if y % 2 != 0:
            x += y
    return x


def multiply(even, odd):
    return even * odd


if __name__ == "__main__":
    n = abs(int(input()))
    
    even = sum_even(str(n))
    odd = sum_odd(str(n))
    result = multiply(even, odd)
    print(result)