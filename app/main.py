from managers.fileManager import *
from managers.cryptManager import *
from vault import *

filePath = "./storage/storage1.txt"

def main():
    os.system('clear')
    checkFileSetup()
    currentUserAuth = getCurrentUserAuth()
    registeredUserAuth = getUserAuth()
    if(currentUserAuth == registeredUserAuth):
        vaultMainMenu()
    else:
        print("Wrong user or password!")
        exit()

if (__name__ == "__main__"):
    main()