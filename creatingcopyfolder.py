import os
def copy_folder_content(source_folder, destination_folder):
    try :
        children=os.listdir(source_folder)
        for i in children:
            sourcechildren=os.path.join(source_folder,i)
            destinationchildren = os.path.join(destination_folder, i)
            if os.path.isfile(sourcechildren):
                with open(sourcechildren,"rb") as sourcecontent:
                    with open (destinationchildren,"wb") as destinationcontent :
                        destinationcontent.write(sourcecontent.read())
            elif os.path.isdir(sourcechildren):
                os.mkdir(destinationchildren)
                copy_folder_content(sourcechildren, destinationchildren)
    except Exception as e:
        print(f"Error {e}")


def conditions():
    
    try:
        inpath=input("kopyalanan qovluğun path-i:").strip()
        outpath=input(" yeni qovluğun path-i").strip()
        if  os.path.exists(inpath)=="False":
            print("Bele bir path movcud deyil")
            return
        if  os.path.isdir(inpath)=="False" :
            print("inpath Folder deyil")
            return
        if  os.path.exists(outpath)=="True":
            print("Bele bir folder artiq var")
            return
        os.makedirs(outpath)
        copy_folder_content(inpath, outpath)
        print(f"{inpath} qovluğu uğurla {outpath}-a kopyalandi.")
    except Exception as e:
        print(f"Error var{e}")
                    
#conditions()
#def copy_folder_content(source_folder, destination_folder):
  #  try :
   #     children=os.listdir(source_folder)
    #    for children in source_folder:
     #       sourcechildren=os.path.join(source_folder,children)
      #      destinationchildren = os.path.join(destination_folder, children)
       #     if os.path.isfile(sourcechildren):
        #        with open(sourcechildren,"rb") as sourcecontent:
         #           with open (destinationchildren,"wb") as destinationcontent :
          #              destinationcontent.write(sourcecontent.read())
           # elif os.path.isdir(sourcechildren):
            #    os.mkdir(destinationchildren)
             #   copy_folder_content(sourcechildren, destinationchildren)
    #except Exception as e:
     #   print(f"Error {e}")