# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("ENTER NAME: ")
age = int(input("ENTER AGE: "))
current_year = 2024
print(f'{name} will turn 100 years in {100-age+2024}')