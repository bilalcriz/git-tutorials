def Sum(uinp):
    if uinp>0:
        i = Sum(uinp-1)
        uinp = uinp + i
        
    return uinp    
        
    
    
    
val = int(input("Enter the val :"))
res = Sum(val)
print(res)