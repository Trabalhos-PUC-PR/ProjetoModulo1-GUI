from stat import filemode
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import AES
from AESCipher import AESCipher
import managers.fileManager as fileMan
from main import filePath
from getpass import getpass

user = ""
passKey = ""

def encryptKey(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.hexdigest()

def encrypt_and_register_Pass(password):
    global passKey
    aesInstance = AESCipher(passKey)
    hashedPass = aesInstance.encrypt(password)
    fileMan.addNewPassword(hashedPass)

def encryptPassword(password):
    global passKey
    aesInstance = AESCipher(passKey)
    return aesInstance.encrypt(password)

def decryptPassword(hashedPass):
    global passKey
    aesInstance = AESCipher(passKey)
    return aesInstance.decrypt(hashedPass)
    
def generateUserToken(username, password):
    global user, passKey
    key = (username+password).encode()
    user = username
    passKey = encryptKey(password.encode())
    return encryptKey(key)