import hashlib

verilenhash=input("Hash-i daxil et: ")
b=input("wordlist-i daxil et: ")
with open ("words.txt","r") as file:
    for line in file :
        soz=line.strip()
        yenihash=hashlib.md5(soz.encode()).hexdigest()
        #print(hashedwords)
        if verilenhash==yenihash:
            print(f'{line} buradadir')
            