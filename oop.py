# class Person:
#   def __init__(self,n,a):
#     self.name = n
#     self.age  = a

#   def __repr__(self):
#     return f'{}'


# p = Person("bilal",23)
# # print(p)

# class Example:
#     def __str__(self):
#         return "This is a string representation"

#     def __repr__(self):
#         return "This is a developer representation"

# obj = Example()

# print(bool(obj)) # Uses __str__ → Output: This is a string representation
# print(repr(obj))   # Uses __repr__ → Output: "'This is a developer representation'"

# class Bilal:
  
#   def __init__(self):
#     self.b=100
#   def setter(a,b):
#     print(a.b)




# b = Bilal()
# b.setter(100)

# def outer(a):
#   print(res)
#   def inner():
#     res =10
#     print(a)
#   inner()

# outer("bilal")

def greet(func):
    def wrapper(a,b):
        print("vankkma mame")
        result = func(a,b)# Call the passed function
        print("varata mame")
        return result  # Modify the result
    return wrapper

@greet
def add(a,b):
    return a+b






print(add(7,8))







