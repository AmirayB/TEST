a=input("1-ci IP address daxil et:")
b=input("2-ci IP address daxil et:")
ip1, subnet1=a.split("/")
ip2, subnet2=b.split("/")
subnet1 = int(subnet1)
subnet2 = int(subnet2)
octet1=ip1.split(".")
octet2=ip2.split(".")
error=0
for i in octet1:
    if int(i) < 0 or int(i) > 255:
        print("XETA(1-ci ip):ip-lerin octet range-i (0,256) arasinda olmalidir", )
        error=1
        break
for j in octet2:
     if int(j) < 0 or int(j) > 255:
         print("XETA(2-ci ip):ip-lerin octet range-i (0,256) arasinda olmalidir")
         error=1
         break
   
if len(octet1)!=4  :
        print(f'1-ci ip address ({".".join(octet1)}) duzgun daxil edilmeyib.')
        error=1
if len(octet2)!=4 :
    print(f'2-ci ip address ({".".join(octet2)}) duzgun daxil edilmeyib.')
if error:
    exit()
if int(subnet1) < 8 or int(subnet1) > 32 or int(subnet2) < 8 or int(subnet2) > 32:
    print("Subnetler 8den kicik ve 32den boyuk ola bilmezler")
    exit()

if int(subnet1)==int(subnet2) :
    if(subnet1>=24):
        if(octet1[0] == octet2[0] and octet1[1] == octet2[1] and octet1[2] == octet2[2]):
            print("Eyni sebekededirler")
        else:
            print("Eyni Sebekede deyiller,router vasitesile elaqe saxlamalidirlar")
    if(subnet1>=16 and subnet1 < 24):
        if(octet1[0] == octet2[0] and octet1[1] == octet2[1] ):
            print("Eyni sebekededirler")
        else:
            print("Eyni Sebekede deyiller,router vasitesile elaqe saxlamalidirlar")
    if(subnet1>=8 and subnet1 < 16):
        if(octet1[0] == octet2[0] ):
            print("Eyni sebekededirler.")
        else:
            print("Eyni Sebekede deyiller,router vasitesile elaqe saxlamalidirlar")
if subnet1 != subnet2:
        print("Subnet maskalari fərqlidir. Router vasitəsilə əlaqə qurulmalidir.")
        exit()
