# find the given number is prime or not return accordingly

import math
import time

def Is_prime(num):


  if num<=1:
    return "Not a prime"
  
  for i in range(2,int(math.sqrt(num)+1)): # sqrt will retuen float so do convert it nto int()
    if num % i == 0:         # Point to note is dont return or assume as soon as this condition fails then the num must be prime and 
      return "Not a Prime"   # dont write a else block here!!! the entire for loop must be failed for this 
  return "Prime"             
  
t0 = time.time()
for i in range(1,100001):
  print(i , Is_prime(i))
t1 = time.time()
print(t1-t0)