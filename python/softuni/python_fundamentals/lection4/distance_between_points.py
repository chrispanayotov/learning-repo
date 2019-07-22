# Write a method to calculate the distance between two points p1 {x1, y1} and p2 {x2, y2}.
# Write a program to read two points (given as two integers) and print the Euclidean distance between them.
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(self, p1, p2):
    dist_a = abs(p1.x - p2.x)
    dist_b = abs(p1.y - p2.y)
    total = sqrt(dist_a ** 2 + dist_b ** 2)
    return total


def create_point(x, y):
    point = Point(x, y)
    return point


x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

distance = calc_distance(p1, p2)
print(f"{distance:.3f}")
