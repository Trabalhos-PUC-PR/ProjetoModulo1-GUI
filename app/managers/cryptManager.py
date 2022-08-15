from stat import filemode
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import AES
from AESCipher import AESCipher
import managers.fileManager as fileMan
from main import filePath
from getpass import getpass

user = ""
passKey = ""
passNonPrintable = ""

def encryptKeyPrintable(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.hexdigest()

def encryptKey(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.digest()

def encrypt_and_register_Pass(password):
    global passKey
    aesInstance = AESCipher(passKey)
    hashedPass = aesInstance.encrypt(password)
    fileMan.addNewPassword(hashedPass)

def encryptPass(password):
    global passKey
    aesInstance = AESCipher(passKey)
    return aesInstance.encrypt(password)

def decryptPassword(hashedPass):
    global passKey
    aesInstance = AESCipher(passKey)
    return aesInstance.decrypt(hashedPass)
    

def getUserAuth():
    file = open(filePath, 'r')
    lines = file.readlines()
    return lines[0].strip()


def getCurrentUserAuth():
    global user, passKey, passNonPrintable
    user = input("Type your username: ")
    passKey = getpass("Type your password (len>=8): ")
    if(len(passKey) < 8):
        print("Password of invalid length! (less than 8 characters)")
        exit()
    key = (user+passKey).encode()
    passKey = encryptKeyPrintable(passKey.encode())
    passNonPrintable = encryptKey(passKey.encode())
    return encryptKeyPrintable(key)

def getPasswords():
    file = open(filePath, "r")
    lines = file.readlines()
    rows = len(lines)-1
    cols = 3
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    cont = 0
    for hashedLine in lines:
        line = decryptPassword(hashedLine.encode())
        passSet = line.strip().split("-")
        if(len(passSet) < 3):
            ...
        else:
            matrix[cont][0] = passSet[0]
            matrix[cont][1] = passSet[1]
            matrix[cont][2] = passSet[2]
            cont+=1
    return matrix