import math

global a, b


def check(a, b):
    print("Euclidean distance from the points a and b to the origin (0, 0)")
    print(math.sqrt(a * a + b * b))


check(7, 5)
check(2, 4)
check(4, 5)
check(3, 2)