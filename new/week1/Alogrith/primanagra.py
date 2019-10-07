from collections import Counter

num = []


def findPrime(n1, n2) :
    for x in range(n1, n2) :
        if x > 1 :
            for n in range(2, x) :
                if (x % n) == 0 :
                    break
            else :
                print(x)
                num.append(x)


start = 0
end = 1000
findPrime(start, end)


def findAnagram(s1):
    # Counter() returns a dictionary data
    for i in range(len(s1)) :
        if Counter(i) == Counter(i + 1) :
            print("! anagram")
        else :
            print(": are not anagram")


findAnagram(num)
