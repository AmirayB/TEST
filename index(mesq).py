metn="In the heart of a misty forest, where sunlight barely touched the ground, there stood an ancient tree older than ..."
print(metn.index("t"))
print("First letter:" , metn[0])
print ("30th letter:", metn[29])
print ("Last Letter:" , metn[-1])
print ("Middle:" , metn[5:] and metn[:-5]) #onden 5 ve sondan 5i atir ele bil ve ortasini verir
print ("Reverse:" , metn[::-1]) #sondaki characterden buyana yazir
print (metn , sep="$")  #coldeki kvadratlari atacaq ve her bosluqa dollar yazacaq
print(type(metn))