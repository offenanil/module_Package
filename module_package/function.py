# error
# print(add(10, 20))
# to solve this we can do in this way, when you write calculator. you can see all the available module

# import calculator
# print(calculator.sub(10, 20))

# Another way we can do as below

# from calculator import add,mul
# print(add(10, 20))
# print(mul(10, 20))

# another way we can all the modules of calculator by putting * sign
# from calculator import *
# print(add(10, 20))

# conflict aries when call the add fuction from calculator and demo
# from calculator import add
# from demo import add
# # conflict arries here
# print(add(10, 20))
# error because both package have same function name add

#to solve this problem
# from calculator import add as MyAdd
# from demo import add
# print(MyAdd(10, 20))

# from lib.helper import message
# print(helper.message())
# but if we use * sign for import, error will arries

# from lib import *
# print(helper.message())
#  to solve this we gonna create __init__.py under lib file after this if we run above file will executed



