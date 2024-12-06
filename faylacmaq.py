f=open("salam.txt","r")
print(f.readline())
print(f.readlines()) #list kimi verir


f.close()
f=open("salam.txt","w+")#write ilenese bir sey yazdiq da overwrtie edir,w+ hem oxumaq hem yazmaq ucun istifade olunur
f.write("salam")
f.writelines("\nsalam",)#writelines a olan da islenir
f.seek(0)#soldan saga kursor yerini deyismek ucundur
print(f.readlines())
f.close()


with open("salam.txt","a+") as f:
    print(f.readlines())
#print(f.readlines())#bu errordur cunki with ile acilsa proses bitende baglanir
#png fomratli fayli acmaq ucun
#with open("random.png","rb") as f:
    #print(f.read())
#Default olan encoding i deyiserik fayl oxumaq
#with open("random.txt","r",encoding="utf-8") as f:
    #print(f.read())