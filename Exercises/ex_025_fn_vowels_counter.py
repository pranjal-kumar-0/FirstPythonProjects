def vowels_counter(string):
    vowels = ['a','e','i','o','u']
    vowels_count = 0
    for char in string.lower():
        if char in vowels:
            vowels_count += 1
    return vowels_count
