#remove an empty tuple(s) form a list of list of tuples

list=list(map(int,input().split(" ")))
list=[t for t in list if t]
print(list)

