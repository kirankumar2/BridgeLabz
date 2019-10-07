import random

ch = int(input("Enter how many time"))
for i in range(ch):
    n = random.uniform(0.0,1.0)
    if n > 0.5:
        print("tail")
    else:
        print("head")
