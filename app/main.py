from fileManager import *
from cryptManager import *

def main():
    checkFileSetup()
    userPassword = getCurrentUserAuth()
    userAuth = getUserAuth()
    if(userPassword == userAuth):
        print("success!")
    else:
        print("Wrong user or password!")
if (__name__ == "__main__"):
    main()