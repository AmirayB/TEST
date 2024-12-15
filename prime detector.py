def is_prime(eded: int) -> bool:
    if eded<=1 :
        return False
    if eded==2 :
        return True
    if eded%2==0 :
        return  False 
    # i=3
    # while i*i   <= eded :
    #     if eded % i == 0:
    #         return False
    #     i += 2  
    for i in range (3,int(eded**0.5+1),2):
        if eded %i ==0 :
            return False
    return True
    



while True:
    eded=int(input("Reqeminizi daxil edin:"))
    res=is_prime(eded)
    print("Eded sadedir" if res else "Eded sade deyil")