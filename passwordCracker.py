import pyzipper

wordlist = "E:\\7th sem\\IS\\passwordDictionary.txt"
file = "E:\\7th sem\\IS\\FINAL450.zip"
fileobject = pyzipper.AESZipFile(file)

with open (wordlist,"rb") as wordlist:
    for word in wordlist:
        try:
            fileobject.pwd = word.strip()
            fileobject.read('FINAL450.xlsx')
        except:
            print("trying password-",word.decode().strip())
            continue
        else:
            print("password found-",word.decode().strip())
            exit(0)
print("No password matched")
