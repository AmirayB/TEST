# var="string".encode("utf-8")
# print(var) #beleli etdik de ise bize yalniz b'string' verir yeni bytlelara cevirmisem kimisinden.
# print(type(var))#goruruk ki bytes classinin uzvudur
# print(list(var)) #her characteri utf-8 formatina cevirdiyi ucun sirf sozu etmir gerek bu cur isledek
# print(var.decode("utf-8"))#string
# print(var[0]) #115
# print(b'string'[0])#115
# ata="aga".encode("ascii")
# print(ata)
# print(list(ata))
# #HEX
# print("string".encode().hex())#737472696e67
# print(b'string'.hex()) #737472696e67
# #print(dir(b'string'))
import base64
print(base64.b64encode("string".encode()))  #b'c3RyaW5n'
#print(base64.b64encode("string")) #bu cur yazma sehvdir cunki binary formatina cevrilmeyib
print(base64.b64encode("string".encode()).decode()) #bu cur yazdiqda ise b herfi de gedir
print(base64.b64decode("c3RyaW5n").decode()) #string aldiq
print(base64.b64decode("c3RyaW5n")) #bu ise bize b'string' verir


import hashlib
soz="amiray"
sozunhashi=hashlib.sha256()
print(sozunhashi,type(hash))

print(hashlib.sha256(soz.encode()).hexdigest()) #encode edib binary formata saliriq ve sha256 ile haslayib hexdigest edirik
#veya
sozunhashi.update(soz.encode())
print(sozunhashi.hexdigest())
print(hashlib.sha256(soz.encode()).digest()) #b'3\xd6\xcf-\x8f\xd7\xbf\xb0\xff\xaf\x1e\xa7\xb1cJ\x9c\xfc\x80\xbb\xf7C\xacf\xf3\x1e\xec\xd0#a\xd8(\x99'
print(hashlib.sha256(soz.encode()).digest().hex()) #eger digest etmisikse sonradan hex edib readable formaya qaytara bilerik yoxsa binary raw verir
print("\xd1")



