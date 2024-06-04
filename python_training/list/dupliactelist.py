#print the list after deleting the duplicate element in it


a=input().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)



a=input().split()
b=list(set(a))
print(b)