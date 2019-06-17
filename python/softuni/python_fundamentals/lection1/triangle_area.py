def triangle_area(base, height):
    return base * height / 2


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    area = triangle_area(a, b)
    print(f"{area:.12g}")