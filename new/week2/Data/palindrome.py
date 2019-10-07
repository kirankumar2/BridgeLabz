import collections
from collections import deque
# from collections import Counter

de = collections.deque([])
se = collections.deque([])
s1 = str(input("enter string 1"))
#de.append(s1)
de.appendleft(s1)
print(de)
s2 = str(input("enter string 2"))
#se.append(s2)
se.appendleft(s2)
print(se)
d = len(s1) + len(s2)
b = sorted(de)
c = sorted(se)
if len(s1) != len(s2) :
    print("not")

elif b == c :
    print('Yes')
else :
    print("no")

# if want to get palindrome with mixed letters
#   for i in range(len(s1)) :
#    for j in range(len(s2)) :
#       if i == j :
#           i += 1
#           print("yes")
#      elif i != j :
#          print("not")

# if Counter(s1) == Counter(s2):
#   print("palindrome")
# else:
#    print("not")
