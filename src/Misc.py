#Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 100

l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
a=[]
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<100]
print(a)
