#sprit,rsprit,lsprit.join,split
#find,rfind,index
#stringescaping



var="strings is very gooood"
print(var.index("i"))
print(var.split()) #default bosluqlara gore ayirir.List qaytarir ("") bele de yaza bilerik.Split list yaradir, sep ise sadece ayirir
print(dir(var)) #bunun sayesinde var variable na tetbiq ede bileceyimiz metodlari goruruk
print("A".join(var.split()))#join elementler arasina elaveler etmek ucundur .
print(var.strip()) #bu sagdan soldan element silmek ucundur meselen metnin sagi ve solu bosluqlardi bu formada sile bilerik,hemcinin "s" yazaram s herfini de siler



print(var.split("i")) #i herfine gore split etdi
print(*var , sep="A")#her herfin arasina A herfini yazacaqdir
print(list(var)) #her herfi ayrisa ayirib list edir
a="""asdnjk
asdsamjdnhak
asdmakl"""
print(a.split("\n"))
b="salam\nsagol"
print(b)
c="     Salam    "
print(c.strip()) #bu sagdan soldan element silmek ucundur meselen metnin sagi ve solu bosluqlardi bu formada sile bilerik,hemcinin "s" yazaram s herfini de siler
print (c.rstrip())#sagdan bosluqlari silecek default
print(c.lstrip())#soldan silecekdir
d="1121Salam1211"
print(d.strip("11"))#sag ve sol
print(d.lstrip("11"))#sol
print(d.rstrip("31"))#sag





#find,rfind,index,rindex
e="Hello world,I am doctor"
print(e.find("o"))
print(e.rfind("o"))
print(e.rindex("o"))
#find index ferqleri deyekki world1 sozunu axtaririq amma ele soz yoxdu bu halda find menfi cavab qaytaracaq index xeta verecekdir.
print(e.replace("doctor","Police"))

#import re

# Örnek metin
#metin = "Python'da 'o' harflerini bulmak çok kolaydır."

# Tüm 'o' harflerini bulma
#o_harfleri = [match.start() for match in re.finditer('o', metin)]

#print("Bulunan 'o' harflerinin indeksleri:", o_harfleri)


#o_sayisi = metin.count('o')
#print("Metindeki 'o' harflerinin sayısı:", o_sayisi)



#stringescaping
print("Kitabin adi 'Sefirlerdir'")#dogrudur
print("Kitabin adi ''Sefirlerdir\" ")#dogrudur
print("Kitabin adi 'Sefirlerdir\"") #dogrudur.
