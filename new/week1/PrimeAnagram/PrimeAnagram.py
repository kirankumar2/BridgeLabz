def rev(l):  # reversing and checking for palindrome
    set1 = set()
    for i in l:
        j = i
        val = 0
        while j > 0:
            rem = j % 10
            val = val * 10 + rem
            j = j // 10
        set1.add(val)
        return set1


def rev1(l):  # reversing and checking for anagram
    set2 = set()
    for i in l:
        j = i
        val = 0
        while j > 0:
            rem = j % 10
            val = val * 10 + rem
            j = j // 10
        if val == i:
            if i > 9:
                set2.add(val)
        return set2

    a = input("enter length")
    set1 = rev(a)
    set2 = rev1(set1)
    print(set2)
