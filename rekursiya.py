def recursiya(n):
    if n < 0:
        return "bele fibonacci yoxdur"
    elif n==0 :
        
        return 0
    elif n == 1:
        return 1
    return recursiya(n - 1) + recursiya(n - 2)
    
    
print(recursiya(2))   