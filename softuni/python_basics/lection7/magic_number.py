magic_number = int(input())

for x1 in range(magic_number+1):
    for x2 in range(magic_number+1):
        for x3 in range(magic_number+1):
            for x4 in range(magic_number+1):
                for x5 in range(magic_number+1):
                    for x6 in range(magic_number+1):
                        if x1 * x2 * x3 * x4 * x5 * x6 == magic_number:
                            print(f"{x1}{x2}{x3}{x4}{x5}{x6} ", end='')