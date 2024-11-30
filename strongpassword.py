password=input("passwordunuzu daxil edin:")
boyukherfler="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kicikherfler="abcdefghijklmnopqrstuvwxyz"
reqemler="0123456789"
xususisimvol="!@#$%^&*()-_+="
counter=len(password)
bcount=0
kcount=0
rcount=0
xcount=0
for i in range(len(password)) :
    if(password[i] in boyukherfler) :
        bcount+=1
    if(password[i] in kicikherfler) :
        kcount+=1
    if(password[i] in reqemler) :
        rcount+=1
    if(password[i] in xususisimvol) :
        xcount+=1
if (bcount>=1 and kcount >=1 and rcount >=1 and xcount>=1 and counter>=8) :
    print("Your password is strong")
if (counter<8) :
    print ("Password minimum 8 characterden ibaret olmalidir")
if (bcount<1) :
    print("En az 1 boyuk herf olmalidir")
if (kcount<1) :
    print("En az 1 kicik herf olmalidir")
if (rcount<1) :
    print("En az 1 reqem olmalidir")
if (xcount<1) :
    print("En az 1 xususi simvol olmalidir")
