import os
import managers.fileManager as fileMan
import managers.cryptManager as cryptMan
import time
import main as main

def vaultMainMenu():
    os.system('clear')
    print(f"Welcome {cryptMan.user}, to the")
    print("""
$$\    $$\  $$$$$$\  $$\   $$\ $$\    $$$$$$$$\ $$\     $$\ 
$$ |   $$ |$$  __$$\ $$ |  $$ |$$ |   \__$$  __|\$$\   $$  |
$$ |   $$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |    \$$\ $$  / 
\$$\  $$  |$$$$$$$$ |$$ |  $$ |$$ |      $$ |     \$$$$  /  
 \$$\$$  / $$  __$$ |$$ |  $$ |$$ |      $$ |      \$$  /   
  \$$$  /  $$ |  $$ |$$ |  $$ |$$ |      $$ |       $$ |    
   \$  /   $$ |  $$ |\$$$$$$  |$$$$$$$$\ $$ |       $$ |    
    \_/    \__|  \__| \______/ \________|\__|       \__|    
                                                          
    """)
    print("                 Your one and only password vault in python\n")
    print("What would you like to do today?\n")
    print("l - List passwords!")
    print("i - Insert a new password!")
    print("d - Delete an existing password!")
    print("e - Edit an existing password!")
    print("n - Delete current user and every password saved inside!")
    print("x - Exit the application!\n")
    selection = input("Please, select an option: ")
    if(selection == 'l'):
        listPasswordMenu()
        vaultMainMenu()
    elif(selection == 'i'):
        insertPasswordMenu()
        vaultMainMenu()
    elif(selection == 'd'):
        deletePasswordMenu()
        vaultMainMenu()
    elif(selection == 'e'):
        editPasswordMenu()
        vaultMainMenu()
    elif(selection == 'n'):
        print("Are you sure?? every password you've saved to this point will be LOST!")
        are_you_sure = input("Are you really, really sure? (y, default = no): ")
        if(are_you_sure != 'y'):
            vaultMainMenu()
        else:
            open(main.filePath, "w").write("")
            print("Exiting the app! Come back again!")
            time.sleep(2)
            os.system('clear')
            exit()
    elif(selection == 'x'):
        print("Exiting the app! Come back soon!")
        time.sleep(2)
        os.system('clear')
        exit()
    else:
        vaultMainMenu()

def listPasswordMenu():
    try:
        passwordSets = fileMan.getPasswords()
    except Exception:
        print("Some of your passwords are corrupted, or have been tampered with, and cannot be loaded")
        selection = input("Do you want this program to delete all corrupt entries? (y/n default = n): ")
        if(selection == 'y'):
            index = fileMan.getCorruptLine()
            while(index != 0):
                fileMan.deletePassword(index)
                index = fileMan.getCorruptLine()
            vaultMainMenu()
        else:
            vaultMainMenu()
        
    if(len(passwordSets) == 0):
        print("You have yet to register a password in the vault!")
        time.sleep(2)
        vaultMainMenu()
    print("Here are your passwords!\n")
    count = 1
    for password in passwordSets:
        print(f"#{count}: Site: {password[0]}, Username: {password[1]}, Password: {password[2]}")
        count += 1
    input("\nPress enter to continue...")
    return len(passwordSets)

def insertPasswordMenu():
    os.system('clear')
    print("Please insert the following information:")
    site = input("From which site is this password? ")
    user = input("What is your username? ")
    password = input("What is your password? ")
    print(f"""
    Site: {site}
    User: {user}
    Password: {password} 
    """)
    selection = input("Is this correct? (y/n default=y): ")
    if(selection == 'n'):
        ...
    else:
        string = site+"-"+user+"-"+password
        cryptMan.encrypt_and_register_Pass(string)

def deletePasswordMenu():
    totalPasswords = listPasswordMenu() + 1
    try:
        index = int(input("Please select the index that will be deleted (enter to return): "))
    except ValueError:
        vaultMainMenu()
    if(totalPasswords <= index or 1 > index):
        os.system('clear')
        print("Invalid index, please try again")
        deletePasswordMenu()
    else:
        fileMan.deletePassword(index)

def editPasswordMenu():
    totalPasswords = listPasswordMenu() + 1
    try:
        index = int(input("Please select the index that will be changed (enter to return): "))
    except ValueError:
        vaultMainMenu()

    if(totalPasswords <= index or 1 > index):
        os.system('clear')
        print("Invalid index, please try again")
        editPasswordMenu()
    else:
        oldPassword = cryptMan.decryptPassword(fileMan.selectPassword(index))
        updatedPass = oldPassword.split("-")
        selection = input("What would you like to change? (s/u/p): ")
        if(selection == 's'):
            updatedPass[0] = input("Please type the updated site: ")
        elif(selection == 'u'):
            updatedPass[1] = input("Please type the updated username: ")
        elif(selection == 'p'):
            updatedPass[2] = input("Please type the updated password: ")
        else:
            vaultMainMenu()
        updatedPass = updatedPass[0]+"-"+updatedPass[1]+"-"+updatedPass[2]
        fileMan.editEntryAt(index, cryptMan.encryptPassword(updatedPass))
        vaultMainMenu()
