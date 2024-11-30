ipaddr=input("IPaddress daxil edin:")
ip,subnet=ipaddr.split("/") 
subnet=int(subnet)
octet=(ip.split("."))
counter=0
error=0
for i in octet :
        counter+=1
        if int(i) not in range (0,256):
            print(f"Octer number {counter},duzgun ip adddress daxil edin.")
            error=1
            break
if len(octet) != 4:
            print("Xəta: IP ünvanı düzgün formatda deyil! (4 oktet olmalıdır)")
if error:
    exit()

    #for i in octet :
        #counter+=1
        #if int(i) not in range (0,256):
            #print(f"Octer number {counter},duzgun ip adddress daxil edin.")
            #error=1
            #break
                  
if  (subnet)>=24 :
                artim=32-int(subnet)
                aralig=2**artim
                subnet_sinifi = int(octet[3]) // aralig  
                networkaddr=octet[:]
                networkaddr[3]=subnet_sinifi*aralig
                broadcastaddr=networkaddr[:]#bir nov kopyasini yaradiriq : bele yazmagimda sebeb ise neyese gore baslayib neyese gore bitirmeden necevarsa ele de copy etmeyi ucundur
    
                broadcastaddr[3]+=aralig - 1

                print(f"Networkaddress: {'.'.join(map(str, networkaddr))}") #map herbirini goturur(meselen ['192', '168', '1', 0, ''] bele bir sey var deyek bunlari string et demisem burada,daha sonra hemin obyektleri join ile birlesdirmisem)
                print(f"Broadcastaddress: {'.'.join(map(str, broadcastaddr))}")
elif 16<=subnet<=24 :
                artim=24-int(subnet)
                aralig= 2**artim
                subnet_sinifi=int(octet[2]) // aralig
                networkaddr=octet[:]
                networkaddr[2]=subnet_sinifi*aralig
                networkaddr[3]=0
                broadcastaddr=networkaddr[:]
                broadcastaddr[2]+=aralig - 1
                broadcastaddr[3]=255
                print(f"Networkaddress: {'.'.join(map(str, networkaddr))}") #map herbirini goturur(meselen ['192', '168', '1', 0, ''] bele bir sey var deyek bunlari string et demisem burada,daha sonra hemin obyektleri join ile birlesdirmisem)
                print(f"Broadcastaddress: {'.'.join(map(str, broadcastaddr))}")
elif 8<=subnet<=16 :
    artim=16-int(subnet)
    aralig=2**artim
    subnet_sinifi=int(octet[1])//aralig
    networkaddr=octet[:]
    networkaddr[1]=subnet_sinifi*aralig
    networkaddr[3]=0
    networkaddr[2]=0
    broadcastaddr=networkaddr[:]
    broadcastaddr[1]+=aralig-1
    broadcastaddr[2]=255
    broadcastaddr[3]=255
    print(f"Networkaddress: {'.'.join(map(str, networkaddr))}") #map herbirini goturur(meselen ['192', '168', '1', 0, ''] bele bir sey var deyek bunlari string et demisem burada,daha sonra hemin obyektleri join ile birlesdirmisem)
    print(f"Broadcastaddress: {'.'.join(map(str, broadcastaddr))}")
else :
    print("/8 den asagi qebul edilmir")



    