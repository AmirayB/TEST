a=input("daxil et")
balaca="?l"
boyuk="?u"
reqem="?d"
symbol="?@"
dec=""
for i in a :
    
    if i.islower():
        dec+=balaca
    elif i.isupper():
        dec+=boyuk
    elif i.isnumeric() :
        dec+=reqem
    else :
        dec+=symbol
print(dec)    

            