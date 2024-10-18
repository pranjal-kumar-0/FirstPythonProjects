#Ask the user for a string and print out whether this string is a palindrome or not.
element = input("Enter a string: ")
if element.lower() == element[::-1].lower():
    print("It is palindrome")
else:
    print("It is not palindrome")