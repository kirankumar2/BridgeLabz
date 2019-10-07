def toString(List):
    return ' '.join(List)


def myfunc(s, l, r):
    if l == r:
        print(s)
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            myfunc(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


string = "ABCD"
n = len(string)
s = list(string)
myfunc(s, 0, n - 1)
