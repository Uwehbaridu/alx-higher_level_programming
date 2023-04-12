#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass(object):
    pass

class MyClass1(object):
    my_attr2 = 3
    def my_method(self):
        pass

print(lookup(Myclass))
print(lookup(Myclass1))
print(lookup(int))
