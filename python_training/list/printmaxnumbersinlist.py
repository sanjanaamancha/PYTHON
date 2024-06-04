a=list(map(int,input().split()))
a.sort()
a.reverse()
print(sum(a[:3]))