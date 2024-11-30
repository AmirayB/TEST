a=input("Soz daxil edin")
elifba="abcdefghijklmnopqrstuvwxyz"
b=list(elifba)
e=[]
key=int(input("Artimi daxil et:"))
encripttext=[]
for i in range(len(a)) :
         c=b.index(i)
         if c+5 >len(b) :
             d=(c+5)%26
             e+=b[d]
             print(e)
         else :
              e += b[c + key]
              print(e)
     