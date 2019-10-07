def bubble(arr):
    # n = int(input("enter the numbers to be sorted"))
    n = len(arr)
    a = "the length is {}"
    print(a.format(n))

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [12, 14, 1, 2, 6, 19,-1]
bubble(arr)
print("the arr is")
for i in range(len(arr)):
    print(arr)
