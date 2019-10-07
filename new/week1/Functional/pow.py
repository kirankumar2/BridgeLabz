import math


def powe():
    n = int(input("enter the pow number"))
    if 0 < n <= 31:
        for i in range(n):
            print(math.pow(2, i))


powe()
