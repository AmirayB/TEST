

dict = {22: "SSH" , 80 : "HTTP" , 25 : "SMTP" , 443 : "HTTPS " , 21: "FTP" , 53 : "DNS"}

while True :
    option=(input("Option number sec : 1(port query), 2(add_service), 3(list all service) or write 'exit' to stop program :"))
    if option.lower() == "exit":
        print("Programi dayandirdiniz")
        break
    

    try:
        option = int(option)
    except ValueError:             #eger integer bir deyer daxil edilmesse bas verecekdir
        print("Duzgun option number daxil edin:")
        continue
    if int(option)==1 :
    
     port = int(input("Portu daxil et: "))
     if port < 1 or port > 65535:
        print("Xəta: Port nömrəsi 1 ilə 65535 arasinda olmalidir.")
        continue
     if port in dict:
        print(f"Port {port} corresponds to {dict[port]}")
     else:
        print(f"Port {port} dictionaryde yoxdur.") 
    #if port < 1 or port > 65535:
               # print("Xəta: Port nömrəsi 1 ilə 65535 arasında olmalıdır.")
                #continue
    elif option== 2 :
         
        
        newport=int(input("Yeni port reqemi:"))
        if newport < 1 or newport > 65535:
         print("Xəta: Port nömrəsi 1 ilə 65535 arasinda olmalidir.")
         continue
        
        if newport in dict :
            print(f"Port {newport} dictionaryde artiq var.")
            continue
        else:
            newservice= str(input("Yeni service adi:"))
            newservice=newservice.upper()
            if newservice in dict.values():
                print(f"{newservice} servisi artiq var.")
                continue
        
        dict[newport]=newservice
        print(f"Service {newservice} added/updated for port {newport}.")
        print(dict)
    elif int(option)==3 :
        print(dict)
    elif option not in range(1,4):
        print("Duzgun option number verin.")
        continue
    
        
    
        

#print(f'daxiletdiyiniz {port} nomresi : {dict.keys}')