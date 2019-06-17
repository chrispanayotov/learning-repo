def math_power(a, b):
    return a ** b


if __name__ == "__main__":
    a = float(input())
    b = float(input())

    result = math_power(a, b)
    print(f"{result}")