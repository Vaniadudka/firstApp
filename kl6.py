# try:
#     print("Test 1 ")
#     print(name)
#     print("Test 2")
# except:
#     print("have error")
#
# else:
#     print("else work")
#
# finally:
#     print("work finally")
#
# print("after try")
#
# def chercker(var1):
#     if type(var1) != str:
#         raise  TypeError("Sorry we need a str type war")
#     else:
#         return var1
#
# chercker("10")


class BuildingError(Exception):
    def __init__(self):
        return "no materials"
def CheckMatirial(amountOfMatirial, limitValue):
    if amountOfMatirial > limitValue:
        return "good"
    else:
        raise BuildingError(amountOfMatirial)

try:
    CheckMatirial(200, 300)

except BuildingError:
    print("buy material")

import warnings

warnings.warn("Warning! Something", SyntaxWarning)