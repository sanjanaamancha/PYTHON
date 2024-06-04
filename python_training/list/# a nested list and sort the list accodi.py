# a nested list and sort the list accoding to the second element in the list
#read a nested list having 2 values in a list.second value of the list should be a number.

n=int(input())
a=[input().split() for i in range(n)]
for i in range(n):
    for j in range(0,n-i-1):
        (a[j][1]>a[j+1],a[j])

print(a)