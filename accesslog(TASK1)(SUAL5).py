try :
   
    set1=set([])
    counter=0
    with open ("access.log", "r") as f :
        for line in f :
            hisse=line.split()
            domain=hisse[2].split(":")[0]
            ip=hisse[1]
            code=hisse[5]
            #print(code)
            if (domain.endswith(".thm") and code=="200"):
                set1.add(ip)
        print(set1)
              

except Exception as e:
    print(f"Unexpected error occurred: {e}")                  
            
            