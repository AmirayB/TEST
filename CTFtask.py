


with open("ctf.txt" , "r") as f:
    list=f.readlines()
    #print(f.read())
    #print(f.readlines())
    for line in list[2:]:
        #print(line)
        newline=line.split(" ")
        #print(newline)
        decoded_line = ""
        for num in newline:
            decode = chr(int(num)) 
            decoded_line += decode
        print(decoded_line)
    if "PassWoRd" in decoded_line:
        print(decoded_line.split()[1])
        
