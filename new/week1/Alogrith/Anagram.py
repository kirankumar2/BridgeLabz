from collections import Counter


def findAnagram(s1, s2):
    # Counter() returns a dictionary data
    if Counter(s1) == Counter(s2):
        print("!", s1, s2, "anagram")
    else:
        print(":( ", s1, s2, "are not anagram")
findAnagram("earth1", "hearte")
findAnagram("cat", "tac")
findAnagram("abcf", "kabc")
