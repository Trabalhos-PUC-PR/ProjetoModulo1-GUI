import managers.fileManager as fileMan
import managers.cryptManager as cryptMan
from getpass import getpass
from vault import *
import time

filePath = "./storage/storage.txt"

def main():
    os.system('clear')
    fileMan.checkFileSetup()

    user = input("Type your username: ")

    passKey = getpass("Type your password (len>=8): ")
    if(len(passKey) < 8):
        print("Password of invalid length! (less than 8 characters)")
        exit()
    currentToken = cryptMan.generateUserToken(user, passKey)
    registeredToken = fileMan.getRegisteredToken()

    if(currentToken == registeredToken):
        vaultMainMenu()
    else:
        print("Wrong user or password!")
        time.sleep(2)
        exit()

if (__name__ == "__main__"):
    main()