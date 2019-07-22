# Write a program to read two rectangles {left, top, width, height} 
# and print whether the first is inside the second. The input is given as two 
# lines, each holding a rectangle, described by 4 integers: left, top, width and height.
# Input: 4 -3 6 4 / 2 -3 10 6; Output: Inside

class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def is_inside(self, other_rect):
        is_in_left = self.left >= other_rect.left
        is_in_right = self.right <= other_rect.right
        is_inside_horizontal = is_in_left and is_in_right

        is_in_top = self.top >= other_rect.top
        is_in_bottom = self.bottom <= other_rect.bottom
        is_inside_vertical = is_in_top and is_in_bottom

        return is_inside_horizontal and is_inside_vertical


def read_rectangle():
    coords = [int(num) for num in input().split(' ')]

    rect = Rectangle(*coords)
    return rect

rect1 = read_rectangle()
rect2 = read_rectangle()

print('Inside' if rect1.is_inside(rect2) else 'Not inside')