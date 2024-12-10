import requests
requests.get("http://google.com")
print((requests.get("http://google.com")).text) #bodysini icerigini getirdi bize cixan neticeni html formatina atsaq run etsek hansi hisseni getirdiyini gore bilerik
cavab=requests.get("http://google.com")
print(cavab.status_code)#status code qaytarir
response=requests.get("http://google.com",params={"param1":"value1"},headers={
    "User-Agent":"Firefox"
})#bunlar bize get ile muraciet etdiyimiz vaxt ozumuzden parametr ve hheaders elave etmeye deyisdirmeye komek edir
#print(response)
print(response.headers) #bu bize qayidan cavabin headerlaridir oz firefox hissemizi gormek isteyirikse
print(response.request.headers) #firefox falan hissesini burada goruruk
print(requests.get("https://google.com",verify=False)) #https sertifkatlarini nezere almamaq ucundur veya gelib import urllib3 deyecik sonrada urllib3.disable_warning() deyecik
print(response.status_code)
for header,value in response.headers.items():#dictionaryni daha seliqeli gormek ucun
    print(f"{header} : {value}")


# #print(requests.get("https://google.com",verify=False, proxies={
#     "http":"127.0.0.1:8082",
#     "https":"127.0.0.1:8082"
# })) # bunun sayesinde burpsutin bu requesti tutmagina ve baxmagimiza icaze veririrk


#json ve post hissesi get de param di postda data

url="http://juice-shop.herokuapp.com/rest/user/login"
body={"email":"test@test.com" ,"password":"password" }
headers={"Content-Type": "application/json"}
response=requests.get(url,json=body)
print(response)


#bezen body hissesine geldikde dictionary kimi oxuya bilmir bunun ucun
import json #bunu da ya json loads ile etmek mumkundur
a=requests.get("http://google.com")
print(a.json())
