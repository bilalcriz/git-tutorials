# find the given number is prime or not return accordingly

# one for loop and one if condition

'''A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. In other words, it has exactly two distinct positive divisors: 1 and itself.

Key Characteristics of Prime Numbers:
Greater than 1: Prime numbers start from 2 (the smallest and only even prime number).

No divisors other than 1 and itself: A prime number cannot be divided evenly by any other number except 1 and itself.

Exactly two factors: A prime number has only two distinct positive divisors.'''

import math
import time

def Is_prime(num):


  if num<=1:
    return "Not a prime"
  
  for i in range(2,int(math.sqrt(num)+1)): # sqrt will retuen float so do convert it nto int()
    if num % i == 0:         # Point to note is-- dont return or assume as soon as this condition fails then the num must be prime and 
      return "Not a Prime"   # dont write a else block here!!! the entire for loop must be failed for this 
  return "Prime"             
  
t0 = time.time()
# for i in range(1,100001):
#   print(i , Is_prime(i))
# t1 = time.time()
print(type(t0))