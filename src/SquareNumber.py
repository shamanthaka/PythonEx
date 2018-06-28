#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)