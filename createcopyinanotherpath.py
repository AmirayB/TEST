import os
a=input("input path:")
b=a
if os.path.exists(a)=="True" :
    if os.path.isfile(a):
        print("Bu filedir")
        os._exit(1)
    else:
        print("Bu folderdir")
else:
    os.mkdir(b)
    print(f"Folder '{b}' yaradildi")        
    
#try:
           
    #os.makedirs(b) 
    #print(f"Folder '{b}' yaradildi")  

#except Exception as e:
    #print(f"Error: {e}")    
