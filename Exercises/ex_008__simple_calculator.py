# Create a Python program that performs basic arithmetic operations (addition, subtraction, multiplication,
# and division) based on user input. Here are the detailed requirements:
#Prompt the user to enter two numbers.
#Prompt the user to enter an operation (addition, subtraction, multiplication, or division).
#Perform the operation and display the result.
#Handle invalid inputs gracefully (e.g., non-numeric inputs for the numbers, invalid operation inputs).
#Avoid division by zero.

num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
operation = int(input('''1. Addition
2. Subtraction
3. Multiplication
4. Division
>>> '''))

if operation == 1:
    print(num1+num2)
if operation == 2:
    print(num1 - num2)
if operation == 3:
    print(num1*num2)
if operation == 4 and num2 == 0:
    print("Not divisible by 0")
if operation == 4:
    print(num1/num2)