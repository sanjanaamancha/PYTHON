#sum of 3 

def my_sum(*args):  #* it is unpacking operator 
    result=0
#iterating over python args tuple
    for x in args:
        result += x
    return result

num=map(int, input().split())
print(my_sum(*num))