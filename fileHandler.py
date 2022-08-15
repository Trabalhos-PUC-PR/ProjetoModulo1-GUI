import os
import struct
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import AES

storagePath = "./storage/storage1.txt"

def main():
    print("Type your password (len>=8): ", end="")
    key = input().encode()
    if(len(key) < 8):
        print("INVALID PASSWORD, TOO WEAK!")
        exit()
    shaInstance = SHA256.new()
    shaInstance.update(key)
    encryptedKey = shaInstance.digest()

    AESinstance = AES.new(encryptedKey, AES.MODE_EAX)
    
    fileSize = os.path.getsize(storagePath)
    print(fileSize)

    with open(storagePath, 'w') as file:
        file.write(struct.pack('<Q', fileSize))

        size = 2048

        


if (__name__ == "__main__"):
    main()