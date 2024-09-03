# Self
# Referring to the parameters after self in the constructor method,
# as arguments just for simplicity.

class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def my_method(self):
        # accessing instance members using self
        print(self.arg1, self.arg2)