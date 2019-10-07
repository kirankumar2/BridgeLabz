from __future__ import print_function
#from PrimeStack.PrimeStack import anagram

def getprime (N, primeArr):  # Print prime or not
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeArr.append(num)

    # **************************************
    def day (self, d, m, y):  # finding the day of week
        y1 = y - ((14 - m) / 12)
        x = y1 + y1 / 4 - y1 / 100 + y1 / 400
        m1 = m + 12 * ((14 - m) / 12) - 2
        d1 = (d + x + ((31 * m1) / 12)) % 7
        return d1

    def week (self):
        for i in week:
            print(i, end=' ')


def leapyear (year):  # check wether year leapyear or not
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        return True
    else:
        return False


# *******************************************
def readfile (fl):
    with open(fl, 'r') as File:  # open file in read mode
        lst = File.read().split()  # Read File and store in list
    File.close()
    return lst


def update (word, fl):
    f = open(fl, "a")  # open file file in append mode
    f.write(" %s " % word)  # write the word in file
    f.close()


def write (list, fl):
    f = open(fl, 'w')  # Open File In write mode
    for item in list:
        f.write("%s " % item)  # Write in the file
    f.close()

def search (self, data):
    self.disply()
    tempnode = self.head
    print(data)
    while tempnode is not None:
        if tempnode.data == data:
            return True
        tempnode = tempnode.next
    return False


def delete (self, data):
    prvnode = tempnode = self.head
    if tempnode.data == data:
        self.head = tempnode.next
    else:
        while tempnode.data != data:
            prvnode = tempnode
            tempnode = tempnode.next
        prvnode.next = tempnode.next


# **********************************************************
def Prime_anagram (primearr):  # finding anagram prime numbers
    for i in primearr:
        primearr.remove(i)
        for j in primearr:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j):
                anagram.append(j)
                anagram.append(j)
                print(i, j)


def getprime (N, primeArr):  # gernerating prime numbers
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeArr.append(num)


# ******************************************************************

# ***************************************************************************
