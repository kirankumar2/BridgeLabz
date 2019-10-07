def MonthlyPayment(p, y, r):
    p = int(input("enter the principle amount"))
    y = int(input("enter the years"))
    r = int(input("enter the percentage"))
    n = 12*y
    r1 = r/(12*100)

    res = (p*r1)/(1-(1+r) ** (-n))
    print(res)


MonthlyPayment(p, y, r)
