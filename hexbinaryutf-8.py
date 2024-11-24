#1 utf-8 2 hex 3 binary

text=input("say something:")
option=int(input("choose option: "))
if option==1 :
    print(text.encode("utf-8"))
elif option==2 :
    print(text.encode().hex())
#elif option==3 :
    
      # for i in text:
       # asc = ord(i)
        #binary=format(asc, "08b")
       
        #print(binary)
elif option==3 :
    binary_output = ' '.join(format(ord(i), '08b') for i in text)
    print(binary_output)