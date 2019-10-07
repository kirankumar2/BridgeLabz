import math


def swapNibbles(x):
    return (x & 0x0F) << 4 | (x & 0xF0) >> 4


x = int(input("enter the number"))
print(swapNibbles(x))

if x % 2 == 0:
    y = math.pow(2, x)
    print(y)
