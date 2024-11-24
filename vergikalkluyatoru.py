illikgelir=int(input("İllik gəlirinizi daxil edin:"))
if illikgelir>=0 and illikgelir<=20000 :
    vergi=illikgelir*5/100
    vergisonrasigelir=illikgelir - vergi
    print("Vergi:",vergi,"AZN")
    print("Vergi sonrasi gelir:",vergisonrasigelir,"AZN")
elif illikgelir>20000 and illikgelir <=50000 :
    vergi=illikgelir*10/100
    vergisonrasigelir=illikgelir - vergi
    print("Vergi:",vergi,"AZN")
    print("Vergi sonrasi gelir:",vergisonrasigelir,"AZN")
else :
    vergi=illikgelir*15/100
    vergisonrasigelir=illikgelir - vergi
    print("Vergi:",vergi,"AZN")
    print("Vergi sonrasi gelir:",vergisonrasigelir,"AZN")
    
    
    
    