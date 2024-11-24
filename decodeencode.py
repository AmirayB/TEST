#UTF-8,ascii,hex,binary,chr,ord,bytes,bytearray,hexlify,string formatting,f string,
#precision {price:.2f},



var="string".encode("utf-8")
print(var) #beleli etdik de ise bize yalniz b'string' verir yeni bytlelara cevirmisem kimisinden.
print(type(var))#goruruk ki bytes classinin uzvudur
print(list(var)) #her characteri utf-8 formatina cevirdiyi ucun sirf sozu etmir gerek bu cur isledek
print(var.decode("utf-8"))#string
print(var[0]) #115
print(b'string'[0])#115


#ascii
isi="string".encode("ascii")
print(isi)
print(list(isi))
#baba=var.encode("ascii")#eger biri ile encode olunubsa yeniden basqasiyla encode ede bilmeyeceyik.
#print(baba)
print(var[0])

#chr,ord

print(ord("s"))#115
print(chr(120))#x
print(chr(11500))#ⳬ
print(chr(116))


#bytes,bytearray
ata="string".encode()
print(bytearray(ata)) #bytearray sonradan indexe esassen characteri deyismek ucundur,bytes ise buna icaze vermir
nik=bytearray("string".encode())
nik[0]=116
print(nik)#birinci simvolu 116ci simvola beraber edecekdir bytes ise buna serait yaratmir
#bik=bytes("string".encode())
#bik[0]=116 #bu xeta qaytaracaqdir.


#HEX
print("string".encode().hex())#737472696e67
print(b'string'.hex()) #737472696e67
#print(dir(b'string'))


#Hexlify
import binascii
print(binascii.hexlify(b'string')) #b'737472696e67'
print(binascii.hexlify(b'string').decode()) #737472696e67 from byte to hex
print(bytes.fromhex("737472696e67").decode())#string from hex to ascii
#print(bytes.fromhex(b'737472696e67').decode()) #bele sey yoxdur

#f string
name="Jhon"
jhon= f"my name is {name}" #bu yol ile formatiing edirik
print(jhon)
exp=f"2+2={2+2}"
print(exp)
A=f"A+A+A+A={'A'*4}" #expression
print(A)
asciivalueofZ=f"Ascii value of Z is={'Z'.encode("ascii")[0]}"#indeksi vermesek b'Z' verecek
print(asciivalueofZ)
asciivalueofB=f"ascii value of B is={ord("B")}"
print(asciivalueofB)


#format
ad="my name is {}"
tezead=ad.format("Jhon") 
print(tezead)

name='my name is {} and i live in {}'
print(name.format("Jhon" , "Mars"))

ixh="my name is {} and i live in {} settlement"
yeniixh=ixh.format("Amiray","Razin")
print(yeniixh)

#precision {price:.2f}
price=100.1573623
print(f"Price is {price:.2f}")
print("Price is {:.2f}".format(price))
print("Price is {price:.2f}".format(price=price))
 # :c unicode , :b  binary , :e :E scientific format :x :X hex , :% percentage format
print(f"Unicode of 110 is {110:c}")
print(f"binary of 110 is {110:b}")
print(f"scientific format of 110 is {110:e}")
print(f"scientific format of 110 is {110:E}")
print(f"hex format of 110 is {110:x}")
print(f"hex format of 110 is {110:X}")
print(f"percentage of 0.4 is {0.4:%}")