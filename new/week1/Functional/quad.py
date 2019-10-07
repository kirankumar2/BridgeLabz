from math import sqrt
a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))
d = (b*b)-(4*a*c)
r1 = ((-b + sqrt(d)) / (2*a))
r2 = ((-b - sqrt(d)) / (2*a))
print("the roots are")
print(r1, r2)

