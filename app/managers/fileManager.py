import time
import managers.cryptManager as cryptMan
import main as main
from getpass import getpass

def addNewPassword(hashedPass):
    file = open(main.filePath, "a")
    file.write("\n")
    file.write(hashedPass.decode())
    file.close()

def deletePassword(index):
    file = open(main.filePath, "r")
    allLines = file.readlines()
    file.close()
    file = open(main.filePath, "w")
    del allLines[index]
    index = len(allLines)
    if(index == 1):
        allLines[index-1] = allLines[index-1].strip()
    file.writelines(allLines)
    file.close()

def selectPassword(index):
    file = open(main.filePath, "r")
    allLines = file.readlines()
    file.close()
    return allLines[index]

def editEntryAt(index, entry):
    file = open(main.filePath, "r")
    allLines = file.readlines()
    file.close()
    file = open(main.filePath, "w")
    allLines[index] = entry.decode() + "\n"
    file.writelines(allLines)
    file.close()

def clearPasswords():
    file = open(main.filePath, "r")
    allLines = file.readlines()
    file.close()
    file = open(main.filePath, "w")
    length = len(allLines)-1
    cont = 1
    while(cont != length):
        del allLines[cont]
        cont += 1
    file.writeLines(allLines)
    file.close()


def checkFileSetup():
    try:
        open(main.filePath, "r")
        if(isNewSetup()):
            setup()
    except FileNotFoundError:
        print("No storage file found! Beggining setup!")
        open(main.filePath, "w")
        setup()

def isNewSetup():
    file = open(main.filePath, 'r')
    lines = file.readlines()
    if(len(lines) == 0):
        return True
    return False

def setup():
    print("Setting up a first time user!")
    username = input("Type your username: ")
    password = getpass("Type your password (len>=8): ")

    file = open(main.filePath, "a")
    tokenHash = cryptMan.encryptKey((username+password).encode())
    file.write(tokenHash)
    file.close()
    
    print("User setup complete!")
    time.sleep(2)
    main.main()

def getRegisteredToken():
    file = open(main.filePath, 'r')
    lines = file.readlines()
    return lines[0].strip()

def getPasswords():
    file = open(main.filePath, "r")
    lines = file.readlines()
    rows = len(lines)-1
    cols = 3
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    cont = 0
    for hashedLine in lines:
        line = cryptMan.decryptPassword(hashedLine.encode())
        passSet = line.strip().split("-")
        if(len(passSet) < 3):
            ...
        else:
            matrix[cont][0] = passSet[0]
            matrix[cont][1] = passSet[1]
            matrix[cont][2] = passSet[2]
            cont+=1
    return matrix

def getCorruptLine():
    file = open(main.filePath, "r")
    lines = file.readlines()
    cont = 0
    for hashedLine in lines:
        try:
            line = cryptMan.decryptPassword(hashedLine.encode())
            cont+=1
        except Exception:
            return cont
    return 0