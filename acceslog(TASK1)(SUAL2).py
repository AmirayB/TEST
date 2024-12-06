try :
   
 uniqueip=set([])
 counter=0
 with open ("access.log", "r") as f :
    for line in f :
        hisse=line.split()
        if len(hisse)>3:
            domainwithport=hisse[2]
            domain = domainwithport.split(':')[0]
            counter+=1
        uniqueip.add(domain)
    print(len(uniqueip))
except Exception as e:
    
    print(f'Golenilmez xeta bas verdi{e}')
        