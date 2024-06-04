#dictionaries

d={'a','b','c','d'}
d=dict.fromkeys(d,10)
print(d)


d={1:'hi', 'a':123, 100:32.4}
print(d.setdefault('a'))
print(d.setdefault('b'))
print(d)
print(d.setdefault('c',200))
print(d)

d={'a':1 ,'b':2, 'c':3,'d':4, 'e':5}
d1={k:v*2 for (k,v) in d.items()}
print(d1)