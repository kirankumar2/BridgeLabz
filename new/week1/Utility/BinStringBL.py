def findString(my_list, fin):
    l = 0
    r = len(my_list)
    while l <= r:
        m = l + ((r - l) // 2)
        res = (fin == my_list[m])
        if res == 0:
            return m - 1
        if res > 0:
            l = m + 1
        else:
            r = m - 1

    return -1


def find(my_list):
    print
    print "Strings are ", my_list
    fin = 'Varun'
    res = findString(my_list, fin)
    if res != -1:
        print "Yes! string found index num = ", res
    else:
        print "String not found"
