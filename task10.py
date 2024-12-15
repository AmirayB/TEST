import random
min=1
max=100
kompnumber=random.randint(1,100)

while True:
    try :
        biz=int(input("Reqemi daxil et:"))
        if biz < 1 or biz > 100:
            print("rəqəm 1 və 100 arasinda olmalidir")
            continue
        if kompnumber==biz :
            print("Tapdiz")
            break
        elif kompnumber > biz :
            print("Kompnumber yuxaridir")
        elif biz>kompnumber :
            print("Kompnumber asagidir")
            
    except Exception as e:
        print(f"Duzgun daxil et:{e}")