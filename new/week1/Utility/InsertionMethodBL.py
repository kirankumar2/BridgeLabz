def insertionSort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i- 1
        while j >= 0 and key < li[j]:
                li[j + 1] = li[j]
                j -= 1
        li[j + 1] = key


my_list = [10, 3, 65, 26, 7, 9, 12, 47]  # Numeric list


def findIntInsertion():
    insertionSort(my_list)
    print
    print "Insertion Sorted integers array is:"
    for i in range(len(my_list)):
        print "%d" % my_list[i]


