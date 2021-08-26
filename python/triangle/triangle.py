def is_triangle(sides: list[int]) -> bool:
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if 0 in sides or (a + b < c) or (b + c < a) or (a + c < b):
        return False

    return True

def equilateral(sides: list[int]) -> bool:
    return is_triangle(sides) and sides[0] == sides[1] and sides[0] == sides[2]


def isosceles(sides: list[int]) -> bool:
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return is_triangle(sides) and ((a == b) or (a == c) or (b == c))


def scalene(sides: list[int]) -> bool:
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return is_triangle(sides) and a != b and b != c
