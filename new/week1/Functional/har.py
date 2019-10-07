n = int(input("enter the harmonic number"))
har = 1.0
for i in range(2, n + 1):
    har += 1 / i
    print(har)
