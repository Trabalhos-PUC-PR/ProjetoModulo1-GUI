from Cryptodome.Hash import SHA256

def encryptKeyPrintable(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.hexdigest()

def encryptKey(key):
    shaInstance = SHA256.new()
    shaInstance.update(key)
    return shaInstance.digest()