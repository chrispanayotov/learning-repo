from math import sqrt

n = int(input())

points_array = []


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show_info(self):
        return f"{self.x};{self.y}"


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.distance = self.calc_distance()
    

    def calc_distance(self):
        dist_a = abs(self.p1.x - self.p2.x)
        dist_b = abs(self.p1.y - self.p2.y)
        total = sqrt(dist_a ** 2 + dist_b ** 2)
        return total
    

    def show_info(self):
        return f"{self.distance:.3f}\n({self.p1.x}, {self.p1.y})\n({self.p2.x}, {self.p2.y})"


def create_point(x, y):
    point = Point(x, y)
    return point


for i in range(n):
    x, y = [int(num) for num in input().split()]
    point = create_point(x, y)
    points_array.append(point)

segment_array = []

for i in range(len(points_array)):
    for j in range(i+1, len(points_array)):
            segment_obj = Segment(points_array[i], points_array[j])
            segment_array.append(segment_obj)

for segment in sorted(segment_array, key=lambda s: s.distance):
    print(segment.show_info())
    break