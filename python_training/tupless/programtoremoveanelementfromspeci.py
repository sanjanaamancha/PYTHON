#program to remove an element from specified index

t=tuple(input.split(','))
l=len(t)
print(l)
i=int(input())
t=t[:i]+ t[i+1:]
print(t)
