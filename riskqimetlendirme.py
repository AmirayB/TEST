tezyiq=int(input("Tezyiqi daxil edin:"))
seker=int(input("Sekeri daxil edin:"))
if tezyiq>140 and seker>120 :
    netice="Yüksək risk — Həkimə müraciət edin."
elif tezyiq>130 and tezyiq<=140 and seker>100 and seker<=120 :
    netice="Orta risk — Müntəzəm yoxlama tövsiyə olunur."
elif   tezyiq<=130 and seker<=100 :
     netice = "Aşağı risk — Sağlamlıq vəziyyətiniz normaldır."
     print("Netice:",netice)
else :
    breakpoint
