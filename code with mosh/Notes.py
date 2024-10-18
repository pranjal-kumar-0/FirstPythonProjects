#STRING METHODS
course = 'Python for Beginners'
len(course)
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("f"))
print(course.replace("Beginners", "Newbies"))
print('Python' in course)
print()

#round fn
print("ROUND")
x = 2.9
print(round(x))
print()

#absolute value == modulus
print("ABSOLUTE")
print(abs(-3.4))
print()

# arithmetic operators
print("ARITHMETIC OPERATORS")
print(5 / 2)
print(5 // 2)  #returns quotient
print(5 % 2)  #returns remainder
print()

#math module
import math

print("MATH MODULE")
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.exp(2))  #e^x function
print(math.pow(2, 3))
print(math.factorial(5))
print(math.sqrt(36))
print(math.pi)
print()

#LIST METHODS
print('LIST METHODS')
L = [1, 2, 3, 3, 4, 4, 5]
print()
L.append(6)
print(L)
L.insert(0, 0)  #index,value
print(L)
L.remove(3)
print(L)
L.pop()  #removes the last item in the list
print(L)
print(L.index(4))  #gives index of the first occurrence of the item
print(L.count(4))  #count of the item
L.sort()  #for ascending order
L.sort(reverse=True) or L.reverse()  # for descending order, L.reverse just reverses the list, so we would have to
# use L.sort() first.
list(set(L))  #remove duplicates, set -> remove duplicates, list -> set back to list
L2 = L.copy()
print(L2)
L.clear()
print(L)
