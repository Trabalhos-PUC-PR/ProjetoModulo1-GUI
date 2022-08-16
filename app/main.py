from managers.fileManager import *
from managers.cryptManager import *
from vault import *
import time

filePath = "./storage/storage.txt"

def main():
    os.system('clear')
    checkFileSetup()
    currentUserAuth = getCurrentUserAuth()
    registeredUserAuth = getUserAuth()
    if(currentUserAuth == registeredUserAuth):
        vaultMainMenu()
    else:
        print("Wrong user or password!")
        time.sleep(2)
        exit()

if (__name__ == "__main__"):
    main()