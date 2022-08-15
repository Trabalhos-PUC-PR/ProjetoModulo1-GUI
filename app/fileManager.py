from getpass import getuser
from cryptManager import encryptKey, encryptKeyPrintable


filePath = "./storage/storage1.txt"

def getPasswordSet():
    file = open(filePath, "r")
    lines = file.readlines()
    rows = len(lines)-1
    cols = 3
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    cont = 0
    for line in lines:
        passSet = line.strip().split("-")
        if(len(passSet) < 3):
            ...
        else:
            matrix[cont][0] = passSet[0]
            matrix[cont][1] = passSet[1]
            matrix[cont][2] = passSet[2]
            cont+=1
    return matrix
    
def getUserAuth():
    file = open(filePath, 'r')
    lines = file.readlines()
    return lines[0]

def isNewSetup():
    file = open(filePath, 'r')
    lines = file.readlines()
    if(len(lines) == 0):
        return True
    return False

def setup():
    print("Type your username: ", end="")
    username = input()
    print("Type your password (len>=8): ", end="")
    password = input()

    file = open(filePath, "a")
    authHash = encryptKeyPrintable((username+password).encode())
    file.write(authHash)
    file.close()
    
    print("Please run this program again to begin saving your passowords!")
    input()
    exit()


def checkFileSetup():
    try:
        open(filePath, "r")
        if(isNewSetup()):
            setup()
    except FileNotFoundError:
        print("NO STORAGE FILE FOUND, BEGGINING SETUP!")
        open(filePath, "w")
        setup()

# print(getPasswordSet())