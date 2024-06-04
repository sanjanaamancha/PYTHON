#WAP to find the factorial of a number using python

n = int(input())
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)