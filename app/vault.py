import managers.fileManager as fileMan
import main as main

def vault():
    print(f"Welcome {fileMan.user}!")
    print("What would you like to do today?")
    print("r - Retrieve passwords!")
    print("i - Insert a new password!")
    print("d - Delete an existing password!")
    print("e - Edit an existing password!")

    