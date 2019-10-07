import math

t = int(input("enter the temp in deg far"))
v = int(input("enter the speed in km/hr"))
if (t < 50) and (v > 3) and (v < 120):
    w = 35.74 + 0.6215 * t + (math.pow(v, 0.16) * ((0.4275 * t) - 35.75))
    print(w)
else:
    print('invalid')