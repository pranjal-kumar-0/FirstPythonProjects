def reverse_string(string):
    reversed_string = ''
    for char in string.lower()[::-1]:
        reversed_string = reversed_string + char
    return reversed_string
