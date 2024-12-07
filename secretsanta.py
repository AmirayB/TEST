import random
#d={"Nuraya":"Seid","Ismayi":"Nicat","Murad":"Amiray","Hikmet":"Banu","Kamran":"Edile"}
sinif = {"Nuraya":None,"Ismayi":None,"Murad":None,"Hikmet":None,"Kamran":None}
adlar= list(sinif.keys())
print(adlar)
#while True:
    # firstname=random.choice(d)
    # secondname=random.choice(d)
    # break
for adam,value in sinif.items():
    alacagi_adam=random.choice(adlar)
    while alacagi_adam==adam :
        alacagi_adam=random.choice(adlar)
    adlar.remove(alacagi_adam)
    sinif[adam]==alacagi_adam
    print(f"{adam} hediyye alir ->{alacagi_adam}")