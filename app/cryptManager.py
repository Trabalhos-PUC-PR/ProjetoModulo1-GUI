from Cryptodome.Hash import SHA256

def encryptKeyPrintable(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.hexdigest()

def encryptKey(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.digest()

def getCurrentUserAuth():
    print("Type your username: ", end="")
    username = input()
    print("Type your password (len>=8): ", end="")
    password = input()
    if(len(password) < 8):
        print("INVALID PASSWORD, TOO WEAK!")
        exit()
    key = (username+password).encode()
    return encryptKeyPrintable(key)