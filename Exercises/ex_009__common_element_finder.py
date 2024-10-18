# Generate two lists and write a program that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your program works on two lists of different sizes.

#generate list a
l_a = []
no_elements_a = int(input("No of elements in A: "))
for i in range(no_elements_a):
    element = int(input("Enter Element: "))
    l_a.append(element)
print()
#generate list b
l_b = []
no_elements_b = int(input("No of elements in B: "))
for i in range(no_elements_b):
    element = int(input("Enter Element: "))
    l_b.append(element)

print()
common_elements = []
for a in l_a:
    for b in l_b:
        if a == b and a not in common_elements:
            common_elements.append(a)

print(f'Common elements: {common_elements}')
