def leap():
    y=int(input("enter year"))

    if (y%4==0):
        if (y%100==0):
            if (y%400==0):
                print("leap")
            else:
                print("not leap")
        else:
                print(" leap")
    else:   
        print("not leap") 
leap()