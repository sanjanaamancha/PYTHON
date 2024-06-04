#default arguments

def myFun(x, y=59):
	print("x: ", x)
	print("y: ",y)
myFun(10)

#keyword arguments

def student(firstname, lastname):
	print(firstname, lastname)
	
student(firstname='cherry', lastname='sam')
student(lastname= 'sam' , firstname='cherry')

#positional arguments

def nameAge(name, age):
	print("Hi I am", name)
	print("My age is", age)

print("case-1:")
nameAge("suraj",27)

print("\nCase-2:")
nameAge(27, "suraj")