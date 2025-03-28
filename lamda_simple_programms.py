#res = lambda a : a * a 
#print(res(10))

# no explicit return statement is needed
# we can pass function as parameters


res = lambda a , b : a if a>b else b
print(res(5,8))