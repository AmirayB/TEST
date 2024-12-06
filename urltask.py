def dogruurl(url, index) :
    try:
        if not url.startswith("http://") and not url.startswith("https://") :
            print(f'{index}-ci URL-i dogru daxil edin:"{url}"')
            return False
        
        if "." not in url :
            print(f"Noqtesiz URL olmur,{index}-ci URL-i duzgun daxil et:'{url}'")
            return False
        
        patterns= " <>#%}|^~{[]`\\ "
        for i in patterns:
            if i in url:
                print(f"{index}-ci URL dogru deyil(xususi simvollar olmaz):{url}")
                return False
       
        domainparts=url.split(".")
        temp=domainparts[1].split(":")[0]
        if len(temp)<2 :     #com org olan hisselerdir bunlar minimum 2character olmalidir bunlarda
            print(f"{index}-ci URL-deki domain duzgun deyil:{url}")
            return False
        
        for part in domainparts :
            if not part :
                print(f"{index}-ci URL-i duzgun daxil edin: {url}")
                return False
    except Exception as e :
        print(f'Xeta bas verdi {e}')
    
    return True
    
#same origin,muqayise
def origin(url):
    
    urlparts=url.split("://",1)#http ve digerlerni ayirdi #1-in menasi ondadir ki bu simvolu 1ci gorduyun yerde split ederek ayir
    protocol=urlparts[0]#http ve https hissesini goturdu
    domainwithport=urlparts[1]#docs.google.com bu tip hisseler qalir ele bil ve qosa noqte qoyub port hissesi slashdan evvel gelir(xatirla)
    
    parts=domainwithport.split(':', 1)
    domain=parts[0]
    portnumber=parts[1] if len(parts)>1 else ""
         
    if portnumber == "" :
        portnumber="80" if protocol=="http" else "443" if protocol=="https" else None
        
    if portnumber and "/" in portnumber:
        portnumber=portnumber.split("/",1)[0]
    return protocol,domain,portnumber

def same_origin(url1,url2):
    has_error=False
    if not dogruurl(url1, 1):
        has_error=True
    if not dogruurl(url2, 2):
        has_error=True
        
    if has_error:
        return 'URL-de xeta movcuddur'
    
    protocol1,domain1,port1=origin(url1)
    protocol2,domain2,port2=origin(url2)
    if protocol1 == protocol2 and domain1 == domain2 and port1 == port2:
        return "Same origin"
    print("Different origin")
    differences=""
    if protocol1 != protocol2 :
        differences+="due to protocol\n"
    if domain1 !=domain2 :
        differences+="due to domain\n"
    if port1 != port2 :
        differences+="due to port"
    return differences

url1 = input("1-ci URL-i daxil edin: ")
url2 = input("2-ci URL-i daxil edin: ")
print(same_origin(url1, url2))