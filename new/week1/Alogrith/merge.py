def merge(liss):
    if len(liss) > 1:
        mid = len(liss) // 2
        left = liss[:mid]
        right = liss[mid:]

        merge(left)
        merge(right)
        i = k = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                liss[k] = left[i]
                i = i + 1
            else:
                liss[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            liss[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            liss[k] = right[j]
            j = j + 1
            k = k + 1


lis = [1, 12, 3, 2, 15, 243, 2]
merge(lis)
print("the sorted list is", lis)
