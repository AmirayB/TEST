import os

def copy_folder_content(source_folder, destination_folder):
    
    try:
        
        children = os.listdir(source_folder)
        for child in children:
            sourcechild = os.path.join(source_folder, child)
            destinationchild = os.path.join(destination_folder, child)

            
            if sourcechild == destination_folder:
                continue

            if os.path.isfile(sourcechild):  
                with open(sourcechild, "rb") as source_file:
                    with open(destinationchild, "wb") as destination_file:
                        destination_file.write(source_file.read())
            elif os.path.isdir(sourcechild):  
                os.mkdir(destinationchild)
                # Rekursiv olaraq qovluğun içindəkiləri kopyala
                copy_folder_content(sourcechild, destinationchild)

    except Exception as e:
        print(f"Xəta baş verdi: {e}")


def conditions():
    try:
       
        inpath = input("Copy etmek istediyiniz path ").strip()
        outpath = input("Hara kopyalamaq istediyiniz path : ").strip()

        
        if not os.path.exists(inpath):  
            print(" Belə  folder yoxdur.")
            return

        if not os.path.isdir(inpath):  
            print(": inpath folder doyul.")
            return

        if os.path.exists(outpath):  
            print(" outpath  mövcuddur.")
            return

        
        os.makedirs(outpath)

       
        copy_folder_content(inpath, outpath)
        print(f"{inpath} folderi {outpath}-e copy olundu.")

    except Exception as e:
        print(f"Error bas verdi: {e}")



if __name__ == "__main__":
    
    conditions()
               