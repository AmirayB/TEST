mebleg=int(input("Məbləği daxil edin:"))
if mebleg>=100 and mebleg<300:
    endirim=mebleg*5/100
    yekunmebleg=mebleg*95/100
    #yekunmebleg=mebleg - endirim (bu curde yazmaq olar)
    print("Endirim:",endirim,"AZN")
    print("Yekun mebleg:",yekunmebleg,"AZN")
elif mebleg>=300:
    endirim=mebleg*10/100
    yekunmebleg=mebleg*90/100
    print("Endirim:",endirim,"AZN")
    print("Yekun mebleg:",yekunmebleg,"AZN")
elif mebleg==0:
    print("Siz hecne satin almamisiz")
    
else :
    print("Endirim tetbiq edilmedi,odenilecek mebleg:",mebleg,"git init AZN")
    
    