from managers.fileManager import *
from managers.cryptManager import *
from vault import *

filePath = "./storage/storage1.txt"

def main():
    checkFileSetup()
    currentUserAuth = getCurrentUserAuth()
    registeredUserAuth = getUserAuth()
    if(currentUserAuth == registeredUserAuth):
        print("Welcome to the vault!")
        vault()
    else:
        print("Wrong user or password!")
if (__name__ == "__main__"):
    main()