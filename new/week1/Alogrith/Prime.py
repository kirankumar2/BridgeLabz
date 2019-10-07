
def findPrime(n1, n2):
    for x in range(n1, n2):
        if x > 1:
            for n in range(2, x):
                if (x % n) == 0:
                    break
            else:
                print(x)


start = 0
end = 1000

findPrime(start, end)


