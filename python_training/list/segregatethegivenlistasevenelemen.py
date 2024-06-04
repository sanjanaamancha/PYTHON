#segregate the given list as even elements first in descending order and then odd elements next in ascending order

a=list(map(int,input().split()))
even=[]
a.sort()
for i in a:
    if i%2==0:
        even.insert(0,i)
    else:
        even.append(i)
print(even)

        
#another method
a=list(map(int,input().split()))
even=[]
odd=[]
for i in a:
    if i%a==0:
        even.append()
    else:
        odd.append()

even.sort(reverse=True)
odd.sort()
print(even+odd)