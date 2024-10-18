#The function should take one string as input and return the length
# of the longest substring that does not contain any repeating characters.
# input: "abcabcdab" output: "abcd"

def longest_unique_substring(str):  #not working
    alphabet_test = []
    alphabet_all_tests = []
    for i in str:
        if i in alphabet_test:
            alphabet_all_tests.append(alphabet_test)
            alphabet_test.clear()
        alphabet_test.append(i)
    for i in alphabet_all_tests:
        max_len = len(alphabet_all_tests[0])
        if len(i) > max_len:
            max_len = len(i)
        return max_len


print(longest_unique_substring("abaabcan"))
