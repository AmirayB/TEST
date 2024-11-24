d=[1,2,2.5,"salam"]
print(*d)
print(*d, sep="\n")
a , b ,c ,e =d    #burada listin her elementi ile eyni sayda variable olmalidir yoxsa xeta qaytaracaqdir
def function():
    print(type(a))
function()   #bu ise functionlardir sonda bu setri yazmalyiq yoxsa funksiya ise dusmur
    
    
    
print(a)
for i in d :
    if isinstance(i, (int,float)):
        print("listdeki reqemlerden  biridir")
    else :
      print("stringdir")
      
f=50
g=29
print (round(f/g , 4), ) #round
print (round (f/g))
 