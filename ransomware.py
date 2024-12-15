import os
import hashlib
import base64
pathver=input("Folder path daxil et:")
if os.path.exists(pathver)==True:
    print("Path dogrudur")
else :
    print("Path yanlisdir")
    if os.path.isdir(pathver)==True:
        print("Daxil etdiyiniz path folderdir")
    else :
        print("path Filedir")
filelar=os.listdir(pathver)
for i in filelar:
    file_path = os.path.join(pathver, i) 
    with open(file_path, "r") as f:
        content=f.read()
        hash=hashlib.sha256(content.encode()).hexdigest()
        print(f.read().split("\n"))
        print(hash)
        
    with open(file_path, 'w') as f:
        f.write(hash)
        print(content)
        
    filead=i.split(".")[0]
    base64_hash = base64.b64encode(filead.decode())
    fullad=base64_hash+i.split(".")[1]
    os.rename(i,fullad)  
    
        
        
        
    
    
    # with open (pathver/i,"w+") as f:
    #     print(f.readlines())
    
#with open (f"{pathver}/"):
    #pass
    