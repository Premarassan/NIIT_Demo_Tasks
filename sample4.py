#Display first n numbers of a Fibonacci series

a=0
b=1
n=int(input())

for c in range(0,n,1):
#while b<"n":
    print(b)
    c=a+b
    a=b
    b=c
    c=a
