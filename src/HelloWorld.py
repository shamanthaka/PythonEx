



n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))




#You can use triple-quoted strings. When they're not a docstring (first thing in a class/function/module), they are ignored.