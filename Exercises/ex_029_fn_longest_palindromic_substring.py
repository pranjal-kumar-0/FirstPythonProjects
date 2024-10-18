def palindrome_checker(substring):
    if substring.lower() == substring.lower()[::-1]:
        return True
    else:
        return False


def longest_palindromic_substring(string):
    string = string.lower()
    palindromic_substrings = []
    i = 0
    z = len(string) + 1
    for k in range(len(string)):
        z -= 1
        for i in range(len(string)):
            i += 1
            result = palindrome_checker(string[i:z])
            if result:
                palindromic_substrings.append(string[i:z])
    print(palindromic_substrings)


longest_palindromic_substring('DABABC')
