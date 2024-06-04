#slicing a list

#L[:]--PRINTS ALL THE ELEMENTS FROM THE LIST
L = [10,11,12,13,14,15,16]
print(L[:])

#L[:2]= prints all the elements from the list starting from index 2
L = [10,11,12,13,14,15,16]
print(L[2:])

L = [10,11,12,13,14,15,16]
print(L[1:6])

#L[::2]--Prints all the elements from the list with step 2(index+2 element from the beginnng)
L = [10,11,12,13,14,15,16]
print(L[::2])
print(L[1:6:3])