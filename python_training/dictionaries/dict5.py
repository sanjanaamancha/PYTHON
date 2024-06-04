#combine 2 dictionary adding values for common keys

from collections import Counter
d={}
d1 = {}
n = int(input())
for i in range(n):
    k=input()
    v=input()
    d[k]=v
    
for i in range(n):
    k=input()
    v=input()
    d1[k]=v

d2 = Counter(d) + Counter(d1)
print(d2)

#another method
'''
dict1={'a':10, 'b':20 , 'c':30}
dict2={'b':5, 'c':15 , 'd':25}
combined_dict={}
for key in dict1:
    if key in dict2:
        comined_dict[key] = dict1[key] + dict2[key]
    else:
        combined_dict[key]=dict1[key]
        
for key in dict2:
    if key not in combined_dict:
        comined_dict[key]=dict2[key]

print("combined dictonary:", combined_dict)'''