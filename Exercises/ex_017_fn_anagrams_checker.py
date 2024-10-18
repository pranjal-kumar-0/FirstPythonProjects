# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

def are_anagrams(str1, str2):
    list1 = list(str1.lower().replace(" ",""))
    for i in list1:
        if i in str2.lower().replace(" ",""):
            list1.remove(i)
        else:
            return False
    return True

