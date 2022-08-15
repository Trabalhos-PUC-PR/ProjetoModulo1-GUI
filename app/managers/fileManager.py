from managers.cryptManager import encryptKeyPrintable
from main import filePath

user = ""
passKey = ""

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
    
    print("User setup complete! Please run this program again!")
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

def getCurrentUserAuth():
    global user, passKey
    print("Type your username: ", end="")
    user = input()
    print("Type your password (len>=8): ", end="")
    passKey = input()
    if(len(passKey) < 8):
        print("Password of invalid length! (less than 8 characters)")
        exit()
    key = (user+passKey).encode()
    passKey = encryptKeyPrintable(passKey.encode())
    return encryptKeyPrintable(key)