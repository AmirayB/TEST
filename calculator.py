#userinput=input("Istediyiniz emeliyyati daxil edin:")
#netice=eval(userinput)
#print(netice)

userinput=input("Istediyiniz emeliyyati daxil edin:")
toplama=userinput.split("+")
cixma=userinput.split("-")
bolme=userinput.split("/")
tambolme=userinput.split("//")
qaliqlibolme=userinput.split("%")

if "+" in userinput :
    #netice=ayirma[0]+ayirma[2]
    #print(netice)
    print(f'netice:{int(toplama[0])+int(toplama[1])}')
elif "-" in userinput :
    print(f'Netice:{int(cixma[0])-int(cixma[1])}')
elif "%" in userinput :
    print(f'Netice:{int(qaliqlibolme[0])%int(qaliqlibolme[1])}')
elif "//" in userinput :
    print (f'Netice:{int(tambolme[0])//int(tambolme[1])}')
else :
      print(f'Netice:{int(bolme[0])/int(bolme[1])}')