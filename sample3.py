#Display the fibonacci series up to a max limit

a=0
b=1
l=int(input())
while b<l:
    print(b)
    c=a+b
    a=b
    b=c
    c=a

