# find the given number is prime or not

import math
import time

def Is_prime(num):

  if num<=1:
    return False
  else:
    return True

num = int(input(("Enter a number:")))
print(type(num))
print(Is_prime(num))