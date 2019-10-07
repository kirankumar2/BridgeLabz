import time

a = int(input("enter 1 to start and 2 to stop"))
if a == 1:
    s =str(time.time())

    for i in range(len(s)):
        b = int(input("enter 2 to stop"))
        if b == 2:
            break

    end = time.time()
    c = end - float(s)
    print(c)
else:
    print("invalid")
