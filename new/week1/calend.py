cal = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
global y1,m1
isTrue = True
while True :
    d = int(input("enter the day"))
    if 1 < d < 31 :

        m = int(input("enter the month"))
        if 1 < m < 12 :
            m1 = (m + 12) * (((14 - m) / 12) - 2)

        y = int(input("enter the year"))
        if -10000 < y < 10000 :
            y1 = (y - (14 - m)) / 12

        x = y1 + (y1 / 4) - (y1 / 100)
        a = d + x + ((31 * m1) / 12) % 7

# formu(d, m, y)
