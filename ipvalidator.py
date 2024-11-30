ip=str(input("Enter ip number:"))
ipdot=ip.split(".")
print(ipdot)

for a in ipdot :
    a=int(a)

    if a>255 or a<0 :
        print("sehv oldu")
        break   
    else :
        print ("ip addrews duzdu")
        
    
    
