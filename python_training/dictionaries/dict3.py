#program to remove a key from a dictionary

d = {}
n = int(input())
for i in range(n):
    k,v = map(int,input().split(" "))
    d[k]=v

key=int(input())
d.pop(key)
print(d)

#output
'''3
1 2
2 3
3 4
2
{1: 2, 3: 4}'''