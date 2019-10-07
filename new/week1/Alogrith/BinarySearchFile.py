class Binary_search:
    def Search(self):  # method search contains reading csv data
        arr = list()
        with open('Book.csv') as fn:  # Opening csv file
            for i in fn:
                for x in i.split():  # splitting word by word in a list
                    arr.append(x)

        res = sortarraylist(arr)
        print(res)
        val = input("Enter Value To Search : ")
        result = binarysearch(0, len(arr) - 1, val, arr)
        if result:
            print("Element Found")
        else:
            print("Element Not Found")


def sortarraylist(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        return arr


def binarysearch(l, r, val, arr):
    while l <= r:
        middle = (l + r) // 2
        if arr[middle] == val:
            return True
        elif arr[middle] < val:
            l = middle + 1
        else:
            r = middle - 1
    return False


if __name__ == '__main__':  # Program gets executes from main
    binary_search = Binary_search()  # creating obj for class binarysearch ()
    binary_search.Search()  # calling search method by using obj
