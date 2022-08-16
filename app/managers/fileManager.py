from managers.cryptManager import encryptKeyPrintable
from main import filePath
from getpass import getpass

def addNewPassword(hashedPass):
    file = open(filePath, "a")
    file.write("\n")
    file.write(hashedPass.decode())
    file.close()

def deletePassword(index):
    file = open(filePath, "r")
    allLines = file.readlines()
    file.close()
    file = open(filePath, "w")
    del allLines[index]
    index = len(allLines)
    if(index == 1):
        allLines[index-1] = allLines[index-1].strip()
    file.writelines(allLines)

def selectPassword(index):
    file = open(filePath, "r")
    allLines = file.readlines()
    file.close()
    return allLines[index]

def insertEntryAt(index, entry):
    file = open(filePath, "r")
    allLines = file.readlines()
    file.close()
    file = open(filePath, "w")
    allLines[index] = entry.decode()
    file.writelines(allLines)


def isNewSetup():
    file = open(filePath, 'r')
    lines = file.readlines()
    if(len(lines) == 0):
        return True
    return False

def setup():
    print("Setting up a first time user!")
    username = input("Type your username: ")
    password = getpass("Type your password (len>=8): ")

    file = open(filePath, "a")
    authHash = encryptKeyPrintable((username+password).encode())
    file.write(authHash)
    file.close()
    
    print("User setup complete! Please run this program again!")
    exit()


def checkFileSetup():
    try:
        open(filePath, "r")
        if(isNewSetup()):
            setup()
    except FileNotFoundError:
        print("No storage file found! Beggining setup!")
        open(filePath, "w")
        setup()