#nested dictionary

d={1:'hi','a':123 , 100:{2:'abc' , 'x': 452, 2.3:120}, 5.4:'python'}
print(d[100]['x'])

student={
    "name": "emm",
    "class": 9,
    "marks":99
}
del student()


d={'a':1 ,'b':2, 'c':3,'d':4, 'e':5}
d1={k:v*2 for (k,v) in d.items()}
print(d1)