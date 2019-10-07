def insertionSort(li):
    for i in range(1, len(li)):
          key = li[i]
          j = i- 1
          while j >= 0 and key < li[j]:
            li[j + 1] = li[j]
            j -= 1
            li[j + 1] = key


def findStrInsertion(my_strings):
    insertionSort(my_strings)
    print
    print "Insertion Sorted Strings array is:"
    for i in range(len(my_strings)):
        print my_strings[i]
