a=input("Reqem daxil et:")
b=input("Reqem daxil et:")
try :
    a=int(a)
    b=int(b)
    bolme=a/b
    print(bolme)
except ZeroDivisionError:
    print("Sifira bolmek emeliyyati duzgun deyil")    
except ValueError :
    print("Reqem daxil edin")
    
    
