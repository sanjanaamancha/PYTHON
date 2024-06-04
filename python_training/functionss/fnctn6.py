
def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)
#user input
num=6
if num>0:
    print(num, recursive_factorial(num))
else: 
    print("no")

