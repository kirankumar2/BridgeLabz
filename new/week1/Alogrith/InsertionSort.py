import re  # imporing reguler expression module


def insertionsort(lis):
    for i in range(1, len(lis)):
        temp = lis[i]
        j = i - 1
        while j >= 0 and temp < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
            lis[j + 1] = temp
    return lis


words = "its my seventh program in Python"
lis = list()
wrd = re.sub("[^\w]", " ", words).split()  # spliting word by word using reguler expression
print(wrd)
res = list()
res = insertionsort(wrd)
print("Sorted is Strings are......")
for i in range(len(res)):
    print(res[i])
