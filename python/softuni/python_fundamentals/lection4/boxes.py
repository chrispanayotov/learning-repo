# Create a class Box, which will represent a rectangular box. 
# Calculate the Perimeter and the Area.
# Input: 0:2 | 2:2 | 0:0 | 2:0; Output: Box: 2, 2, Perimeter: 8, Area: 4
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    @staticmethod
    def calc_distance(p1, p2):
        dist_a = abs(p1.x - p2.x)
        dist_b = abs(p1.y - p2.y)
        total = sqrt(dist_a ** 2 + dist_b ** 2)
        return int(total)


class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.width = self.get_width()
        self.height = self.get_height()


    def get_width(self):
        width = Point.calc_distance(self.upper_left, self.upper_right)
        return width
    

    def get_height(self):
        height = Point.calc_distance(self.upper_left, self.bottom_left)
        return height


    def calculate_perimeter(self):
        return ((2 * self.width) + (2 * self.height))


    def calculate_area(self):
        return self.width * self.height

    
    def show_info(self):
        return f"Box: {self.width}, {self.height}\nPerimeter: {self.calculate_perimeter()}\nArea: {self.calculate_area()}"


def create_point(input_):
    x, y = [int(num) for num in input_.split(':')]
    point = Point(x, y)
    return point


def create_box(upper_left, upper_right, bottom_left, bottom_right):
    upper_left = create_point(upper_left)
    upper_right = create_point(upper_right)
    bottom_left = create_point(bottom_left)
    bottom_right = create_point(bottom_right)

    box = Box(upper_left, upper_right, bottom_left, bottom_right)
    return box


data = input().split(' | ')
box_list = []

while data[0] != 'end':
    box = create_box(data[0], data[1], data[2], data[3])
    box_list.append(box)

    data = input().split(' | ')

for box in box_list:
    print(box.show_info())