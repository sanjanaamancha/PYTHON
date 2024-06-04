#dictionaries

d= {1:'hi' , 'a':123 ,100:32.2}
print(d[1])
print(d['a'])
print(d[100])
print(d.get('a'))
for i in d:
    print(i, ":",d[i])

x= {1:'hi' , 'a':123 ,100:32.2}
x[1]=1000
print(x)
del x[1]
print(x)

d= {1:'hi' , 'a':123 ,100:32.2}
print(d.get(100))
d.update({1})