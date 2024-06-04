#read a list and print sum of 3 min elements in list

a=list(map(int,input().split()))
b=[]
for i in range (len(a)):#
    if i not in b:
        b.append(i)
a.sort()
c=sum(b[:3])
print(c)

a=list(map(int,input().split()))
a.sort()
print(sum(a[:3]))

a=list(map(int,input().split()))
a.sort()
print(sum(a[3:]))
