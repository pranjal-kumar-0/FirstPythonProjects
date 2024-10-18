list_A = []
no = int(input("No of elements to be entered in list: "))
for i in range(no):
    element = int(input("ENTER NUM: "))
    list_A.append(element)

largest_num = list_A[0]
for i in list_A:
    if i > largest_num:
        largest_num = i

print("Largest Num: " + str(largest_num))