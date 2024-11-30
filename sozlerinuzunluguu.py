userinput=input("Metn daxil et:")
sozler=userinput.split(" ")
for soz in sozler : #i=soz
    if len(soz)>5 :
        userinput = userinput.replace(soz, "long")
        print (userinput)
samitler = "bcçdfgğhjklmnprsştvyzqwx"  # Azərbaycan dilində samitler
neticem = ""
for herf in userinput:
    if herf.lower() in samitler:  #eger inputdaki samitler balacadirsa,samitler variable'indaki lerde balaca oldugundan upper formasini elave et deyilem else onlari oldugu kimi saxla deyirem
        neticem += herf.upper()  
    else:
        neticem += herf  

print("Nəticə:", neticem) 

    

    