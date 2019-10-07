def temperaturconversion():
    a = int(input("enter if u want to convert from c-f type 1 or enter if u want to convert from f-c type 2"))

    if a == 1:
        c = float(input("enter the temp in c"))
        z = (c * (9 / 5)) + 32
        e="temp in f is {}"
        print(e.format(z))

    if a == 2:
        d = float(input("enter the temp in f"))
        y = int((d - 32) * (5 / 9))
        x="temp in c is {}"
        print(x.format(y))

    else:
        print("invalid")


temperaturconversion()
