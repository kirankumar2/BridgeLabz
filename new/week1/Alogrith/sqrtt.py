
c = int(input("enter the value of c"))
t = c
epsilon = 1e-15
e = (1 * epsilon) - 15
while abs(t - (c / t)) > epsilon * t:
    t = ((c / t) + t) / 2


print(t)
