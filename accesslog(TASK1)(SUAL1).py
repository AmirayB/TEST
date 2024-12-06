
try :
   
 uniqueip=set([])
 with open ("access.log", "r") as f :
    counter=0
    for line in f :
        hisse=line.split()
        #print(hisse[1])
        if len(hisse)>3 and hisse[3]=="CONNECT" :
            counter+=1
            ip=hisse[1]
        uniqueip.add(ip)
    print(f"muraciet eden umumi source:{len(uniqueip)}")
    print(f'Proxy servere gelen sorgu sayi:{counter}')
except Exception as e :
    print(f'Xeta bas verdi:{e}')



            
   