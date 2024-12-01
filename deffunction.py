def code(info,encoding='UTF-8'):
    if encoding=='UTF-8':
        return [i.encode('UTF-8') for i in info]
    elif encoding == 'hex':
        return [i.encode('UTF-8').hex() for i in info]
    else:
        return "Duzgun encoding sec"
        
i=input("MEtninizi daxil edin:")
b=input("Encoding formati daxil edin:")

if not b :
    print (code(i))
print(code(i,b ))