def find(arr):          # find sort method to sort strings
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def findStrSort(arr):   # find sort method definition
    find(arr)
    print
    print
    print "Bubble Sorted String array is:"
    for i in range(len(arr)):
        print  "%s" % arr[i]