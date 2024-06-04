#SUM OF FIRST N NATURAL NUMBERS USING A LOOP

n = int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)