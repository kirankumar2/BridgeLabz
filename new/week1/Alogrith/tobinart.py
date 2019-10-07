def dec(n) :
    return bin(n).replace("0b", "")


if __name__ == '__main__':
    print(dec(int(input("enter the number"))))
