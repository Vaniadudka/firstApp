import colorama

print(help(colorama))

cl = colorama

print(cl.__name__)
print(type(cl))

name = ""
for method in dir(name):
    print(method)

print(hasattr(name, "index"))
print(hasattr(name, "initialise"))