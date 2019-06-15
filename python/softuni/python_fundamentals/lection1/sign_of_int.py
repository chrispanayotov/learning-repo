def define_number(num):
    if num < 0:
        return f"The number {num} is negative."
    elif num == 0:
        return f"The number 0 is zero."
    else:
        return f"The number {num} is positive."


if __name__ == "__main__":
    number = int(input())
    print(define_number(number))