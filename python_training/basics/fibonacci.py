#WAP to print fiboncci series upto n terms

n = int(input())
fib = [0,1]
for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])
print(fib)

##another method
n = int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b, a+b