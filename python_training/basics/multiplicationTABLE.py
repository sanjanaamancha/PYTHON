#WAP to print the multiplication table ofa given number

def table(n):
    for i in range(1,11):
        print(n," * ",i,"=",n*i)
n = int(input())
table(n)
