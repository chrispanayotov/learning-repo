def print_lines(length):
    print("-" * 2 * length, end='')
    print()


def print_interior(length):
    for i in range(n-2, 0, -1):
        print("-",end='')
        for j in range(n - 1):
            print("\\/", end='')
        print("-", end='')
        print('')
    

if __name__ == "__main__":
    n = int(input())
    print_lines(n)
    print_interior(n)
    print_lines(n)