'''def factorial_iterative(num):
    # returns the factorial of a given number
    result = 1
    for i in range(1,num+1):
        result *= i
    return sum
        
    
    
ui = int(input("Enter a valid integer :"))
print(factorial(ui))'''

# method 2
# limitation -- stackoverflow

import sympy

# def factorial_recursive(num):
#     if num == 1:                # base case
#         return 1
#     return num * factorial(num-1) ## recursive case # recursive call (i.e for each recursive call it will add up a new stack)
        
    
    
ui = int(input("Enter a valid integer :"))
print(sympy.factorial(ui))
