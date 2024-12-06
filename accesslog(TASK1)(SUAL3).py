try :
   
 uniquecode=set([])
 counter=0
 with open ("access.log", "r") as f :
    for line in f :
        hisse=line.split()
        if len(hisse)>6 :
            status_code = hisse[5]
        uniquecode.add(status_code)
    print(uniquecode)
except Exception as e :
    print(f"Xeta bas verdi:", e)
            
        