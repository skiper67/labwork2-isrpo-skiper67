import math

def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r

def square_area(a):
    return a * a

def square_perimeter(a):
    return 4 * a

def rectangle_area(a, b):
    return a * b

def rectangle_perimeter(a, b):
    return 2 * (a + b)

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def triangle_perimeter(a, b, c):
    return a + b + c
