def years(a,b):
    years = 0
    while a<b:
        a *=3
        b *=2
        years +=1
    return years
print(years)

a,b = map(int,(input().split(" ")))
years(a,b)