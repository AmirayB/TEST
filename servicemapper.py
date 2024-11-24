

dict = {22: "SSH" , 80 : "HTTP" , 25 : "SMTP" , 443 : "HTTPS " , 21: "FTP" , 53 : "DNS"}

while True :
    option=int(input("Option number sec : 1(port query), 2(service), or 3(list all service)"))
    
    if option==1 :
        port=int(input("Portu daxil et:"))
        print(f"Port {port} corresponds to {dict[port]}")
    elif option== 2 :
        
        newport=int(input("Yeni port reqemi:"))
        
        if newport in dict :
            print(f"Port {newport} dictionaryde artiq var.")
            continue
        else:
            newservice= str(input("Yeni service adi"))
            if newservice in dict.values():
                print("Bu servis artiq var")
                continue
        
        dict[newport]=newservice
        print(f"Service {newservice} added/updated for port {newport}.")
        print(dict)
    elif option==3 :
        print(dict)
    else :
        break
        

#print(f'daxiletdiyiniz {port} nomresi : {dict.keys}')