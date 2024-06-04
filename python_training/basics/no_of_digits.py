
number = int(input())
count = 0
while number != 0:
    number //= 10
    count +=1
print("no.of digits:" , count)