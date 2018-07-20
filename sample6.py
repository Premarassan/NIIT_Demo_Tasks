#A program that generates all prime numbers between x and y

x=int(input())
y=int(input())
#n=int(input())

for a in range(x,y):
    if a > 1:
        for b in range(2,a):
            if(a%b) == 0:
                break
        else:
            print(a)
    
