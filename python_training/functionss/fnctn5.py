#to print a factoiral of a number recursively

def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n* recursive_factorial(n-1)
#user input
num=6

#check if input is valid or not
if num<0:
    print("invalid input ! please enter a positive number.")
elif num==0:
    print("Factorial of number 0 is 1")
else:
    print("factorial of number", num, "=", recursive_factorial(num))
