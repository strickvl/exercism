def is_triangle(sides: list[int]) -> bool:
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return 0 not in sides and a + b >= c and b + c >= a and a + c >= b

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
