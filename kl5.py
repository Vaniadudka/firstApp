import sys

import requests
#
# print(help(requests))


def fifrst_func():
    pass

class Human:
    pass

rq = requests
first_f = fifrst_func
nick = Human

print(rq.__name__)
print(first_f.__name__)
print(nick.__name__)

print(type(rq))
print(type(first_f))
print(type(nick))


name = ""
for method in dir(name):
    print(method)


print(hasattr(name, "reverse"))
print(hasattr(name, "index"))

print("getattr - ")
print(getattr(name, "startswith"))


print(callable(name))
print(callable(fifrst_func()))

class A:
    pass

class B(A):
    pass

print(isinstance(A, B))

print(isinstance(B, A))

object1 = B()
print(isinstance(object1, B))

import inspect

print(inspect.ismodule(inspect))
print(sys.version)
print(sys.platform)