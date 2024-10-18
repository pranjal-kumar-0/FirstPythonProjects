#Create a program that asks the user for a number and then prints out a
# list of all the divisors of that number.

num = int(input("ENTER A NUMBER TO CHECK ITS FACTOR: "))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print(divisors)
