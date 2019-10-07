import math


def findNum(high, low):
    while high >= low:
        mid = (low + high) / 2
        print("if found=1 / if less=2 /if greater=3")
        print("Your num is ?", mid)
        ch = int(input())
        if ch == 1:
            print(mid)
            break
        else:
            if ch == 2:
                high = mid - 1
                print("Your num is ?", mid)
            else:
                low = mid + 1
                print("Your num is ?", mid)


num = int(input("Enter a num 0 -5"))
ele = int(math.pow(2, num))
low = 0
high = ele
print("low", low, "high", high)
findNum(high, low)
