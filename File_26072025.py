# global and local variable
# inheritance
# string manipulation
# class variables

def outer_function():
    x = 10
    print(f"Outer {x}")
    def inner_function():
        x = 20
        print(f"inner {x}")
    inner_function()

outer_function()

class parent():
    parent_var_class = "This variable is from the parent class"
    def __init__(self):
        print(f"Printing from Parent class {self.parent_var_class}")

class child(parent):
    child_class_var = "This is from child class"
    def __init__(self):
        super().__init__()
        print(f"printing from child class {self.child_class_var} and {self.parent_var_class}")


a = child()
print((child.__mro__))
print((child.mro()))