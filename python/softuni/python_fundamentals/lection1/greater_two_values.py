def comparison(data_type):
    if data_type == "int":
        print(compare_int(a, b))
    else:
        print(compare_str(a, b))


def compare_int(a, b):
    a = int(a)
    b = int(b)
    if a > b:
        return a
    return b


def compare_str(str_a, str_b):
    x = 0
    y = 0
    for i in range(len(str_a)):
        x += ord(str_a[i])

    for j in range(len(str_b)):
        y += ord(str_b[j])

    if x > y:
        return str_a.title()
    return str_b.title()


if __name__ == "__main__":
    input_type = input()
    a = input()
    b = input()
    comparison(input_type)