def count_characters(string):
    chars_count = {}
    for i in string:
        if i in chars_count:
            chars_count[i] += 1
        else:
            chars_count[i] = 1
    return chars_count
