#Q.1 function for calculating area of circle
def area():
    radius=float(input("enter a radius of circle"))
    area=3.14*radius*radius
    print(area)
area()


#Q.2 function using for perfect number between 1 to 1000.
def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum=sum + i
    if sum==n:
        return True
    else:
        return False
for i in range(1,1001):
    if perfect(i):
        print(i)

#Q.3. print the multiplication table of 12 using recursion.
def table(n,i):
     print(n*i)
     i=i+1
     if i<=10:
         table(n,i)
table(12,1)

#Q.4 using recursion calculate power.
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
print (power(8,3))


#Q.5 write a function to find factorial and stored in dictionary.
def factorial(n):
    if n<=1:
        return 1
    else:
        return (n*factorial(n-1))
n=int(input("enter the number n: "))
print("factorial: ")
print(factorial(n))
a=factorial(n)
l="output"
d={}
d[l]=a
print(d)
