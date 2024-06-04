s={3,1,2,4,6,7}
print(set(sorted(s)))

s1={10,20,30,40,50}
s2={60,70,10,30,40,80,20,50}
print(s1.issubset(s2))
print(s2.issuperset(s1))

res={s for s in [1,2,3] if s %2}
print(res)
