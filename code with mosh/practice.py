s1 = float(input("Enter the first side of the triangle: "))
s2 = float(input("Enter the second side of the triangle: "))
s3 = float(input("Enter the third side of the triangle: "))
p = (s1 + s2 + s3)
s = p/2
area = (s * (s-s1) * (s-s2)*(s-s3))**0.5
print("The perimeter of the triangle is : {0:.2f}".format(p))
print("The area of the triangle is : {0:.2f}".format(area))
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)
pc=2*PI*r
print('perimeter of circle=%.2f' %pc)