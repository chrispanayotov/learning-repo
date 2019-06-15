def print_top(n):
    for row in range(1, n+1):
        for col in range(1, row+1):
            print(col, end=' ')
        print()


def print_bottom(n):
    for row in range(1, n):
        for col in range(1, n-row+1):
            print(col, end=' ')
        print()


def print_triangle(n):
    print_top(n)
    print_bottom(n)


if __name__ == "__main__":
    num = int(input())
    print_triangle(num)