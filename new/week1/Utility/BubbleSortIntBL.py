def find(arr):       # find method definition to sort elements using bubble sort
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def findSort(arr):  # findsort method definition
    find(arr)
    print
    print ("Bubble Sorted Int array is:")
    for i in range(len(arr)):
        print arr[i]
