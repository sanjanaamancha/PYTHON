#program to map 2 lists into a dictionary

a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
d={ a[i]:b[i] for i in range(len(a)) }
print(d)

'''another method
keys=input().split()
values=input().split()
d=dict(zip(keys, values))
print(d)'''

''' 
l1=[1,2,3]
l2=[4,5,6]
d={}
for i in range(0,3):
    key=l1[i]
    value=l2[i]
    d[key]=value
print(d)'''



'''output for 1st code
1 2 3
4 5 6
{1: 4, 2: 5, 3: 6}'''