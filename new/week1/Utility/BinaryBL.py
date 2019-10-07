def makeSort(my_list):  # Calling makesort to sort list
    my_list.sort()
    print my_list  # printing


def findBinary(my_list, l, r, key):  # doing binary search operation
    if r >= l:
        mid = l + (r - l) / 2
        if my_list[mid] == key:
            return mid
        elif my_list[mid] > key:
            return findBinary(my_list, l, mid - 1, key)  # Recalling same method
        else:
            return findBinary(my_list, mid + 1, r, key)
    else:
        return 1


def find(my_list):
    print
    makeSort(my_list)  # calling make sort method
    key = 47
    result = findBinary(my_list, 0, len(my_list) - 1, key)  # calling find binary method method to find key value in list

    if result != 1:  # result of method which return wether element found or not
        print "Element is present at index % d" % result
    else:
        print "Element is not present in array"
