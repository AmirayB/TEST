try :
   
 suspicious={}
 counter=0
 with open ("access.log", "r") as f :
    for line in f :
        hisse=line.split()
        domain=hisse[2].split(":")[0]
        if domain.endswith(".thm"):
            suspicious[domain] = suspicious.get(domain, 0) + 1
            if suspicious[domain] > counter:
                counter = suspicious[domain]
                highcount = domain
        #if domain.endswith('.thm') :
         
         #suspicious[domain]=0
         #suspicious[domain]+=1
         #break
    print(suspicious)
    print(highcount)
    
    if highcount:
        print(f"The suspicious domain with the highest connection attempts is: {highcount}")
        print(f"Connection attempts: {counter}")
    else:
        print("No domains ending with .thm found in the log.")
    #if suspicious:
        #maxcount=0
       # for domain,count in suspicious.items() :
             #if count > maxcount:
                #suspicious_domain = domain
        #max_count = count
        #print(f"The suspicious domain with the highest connection attempts is: {suspicious_domain}")
       # print(f"Connection attempts: {suspicious[suspicious_domain]}")
except Exception as e:
    print(f"Gozlenilmez xeta bas verdi {e}")