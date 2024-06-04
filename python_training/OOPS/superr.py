#super method

class Parent:
    def func1(self):
        print("this is function1")
class Child(Parent):
    def func2(self):
        super().func1()
        print("this is function2")

ob=Child()
ob.func2()