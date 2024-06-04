#find the repeated items of a tuple

t=tuple(input().split(" "))
c=0
for i in t:
    if t.count(i)>c:
        c=t.count(i)
        a=i
print(c)
print(a)