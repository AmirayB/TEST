#list,append,remove,pop,count,copy,insert,sort,del,string-list,list-string,tuple,dictionary,set,try-except bloklari


lst=[]
lst.append(1)
print(lst)
lst2=[3]
lst2 +=lst
print(sorted(lst2))
lst2.pop(1) #elemente gore silir
print(lst2)

lst3=["salam"]
lst4=["necesen"]
lst4+=lst3
(lst4.pop(0))#string daxil edildik de indexe gore ile bilirik.
print(lst4)
print(lst4.count("salam",))
lst4.append(1)

lst3=lst4.copy() #copy array i bir basa kopyalayir lakin sonradan etdiyimiz deyisiklik yansimir
print(lst3)
lst4.append(2)
print(lst4)
print(lst3)

lst3=lst4
lst4.append(6)
lst3.append(10)
print(lst3)
print(lst4)
lst3.insert(3,"salam2")#muvafiq indexe element elave etmek ucun
print(lst3)
print(lst4)
lst3.pop(0)
lst3.remove("salam2")
lst3.sort()
print(lst3[::-1]) #reverse ucun
lst3.sort(reverse=True)#reverse ucun
print(lst3)
print(sorted(lst3))
del(lst3) # listi bir basa silir
#print(lst3)
print(lst4)
del lst4[0] #muvafiq indexi silmek ucun
print(lst4)
lst5=[50,60] #listi decode etdik
print(bytes(lst5).decode())
print("2<".encode())
lst10=[]
for i in "2<".encode() : #liste cevirdik
    lst10.append(i)
    print(lst10)


tup1=(1,3)  
tup2=(2,4)
tup1+=tup2
print(tup1)   #immutabledir 

def func():
    return 1,2
print(func())



dict1={"key1":1 ,"key2":3, "key3":"Salam"}
print(dict1["key1"])
dict1["key3"]= 2
dict1["key4"]=400
print(dict1["key4"])

dict2={"key1":1 ,"key2":3, "key3":"Salam","key4":[0,1,2,3,],"key5":{"key6":"qaqa"}}
print(dict2["key4"][2])#index
print(dict2["key5"]["key6"])#ic ice oldugu halda
dict2.popitem() #default sonuncunu silir
dict2.pop("key1")#key-e esesen silir
print(dict2)
#a=input("key daxil et:")
#b=input("value daxil et:")
#dict2[a]=b
print(dict2)

#b=input("new value:")
#dict2["ismayil"]=b
print(dict2)
print(dict1)
dict1.update(dict2)
print(dict1)
print(dict1.keys())

dict5={"key1":1 ,"key2":3, "key3":"Salam","key4":[0,1,2,3,],"key5":{"key6":"qaqa"}}
print(dict5.keys())
print(dict5.values())


#set
set1=set([1,2,3,4])
print(set1)
set1.add(5)
print(set1)
set1.remove(3)
#set1[0]=5 #error
print(set1)
for i in (range(70,80)[::-1]) :#reverse olur veya colden reversed etmeleyik
    print(i)
for i in range(0,5,2):
    print(i)
for i in range(0,10,2):
    if i==6 :
        continue
    print(i)
for i in range(0,10,2):
    
    if i==6 :
        break
    print(i,"burdayiq")
#for-da else de var for isini bitirenden sonra avamatik else kecir
try: #tryda meqsed iceride kod yazanda erroru gormeden nese cap etmekdir
    a=5
    b=0
    c=a/b
    print(c)
except :#bu formada da yaza bilerik veya erroun adina uygun da vere bilerik.
    print("Problem var")
    
    
    
try: 
    a=5
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Problem var")
    
try:
    x=5
    d=x
    print(d)
except NameError:
    print("evvelceden x tanimlanmiyinb")
try :
    ad="ALI"
    value=ad[1]
except IndexError:
    print("index error var")
else:#try blokunda problem yasanmasa bu da icra olunacaqdir
    print("Hersey qaydasindadir") 
finally:#bu ise xeta olsada olmasada icra olunur
    print("xeta maraqli deyil")
#mesel ucun a=5 b=0 vermisik lakin bolendeki erroru exceptde catmadan almaq isteyirikse raise dan istifade ederik
try:
    a=5
    b=0
    if b==0 :
        raise ZeroDivisionError
    c=a/b
except ZeroDivisionError :
    print("Zerodovission error var")
try :
    a=5
    b=2
    c=a/b
    x=5
    d=x
    ad="Amiray"
    value=ad[9]
except Exception as e:#bu ise erroru e variablena beraber edir.
    print(e)