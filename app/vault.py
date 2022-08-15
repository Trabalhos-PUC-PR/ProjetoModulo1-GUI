import os
import managers.fileManager as fileMan
import managers.cryptManager as cryptMan

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
    print("What would you like to do today?\n")
    print("l - List passwords!")
    print("i - Insert a new password!")
    print("d - Delete an existing password!")
    print("e - Edit an existing password!")
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
        ...
    elif(selection == 'x'):
        print("Exiting the app! Come back soon!")
        exit()
    else:
        vaultMainMenu()

def listPasswordMenu():
    passwordSets = cryptMan.getPasswords()
    if(len(passwordSets) == 0):
        print("you have yet to register a password in the vault!")
        input("Press enter to continue...")
        vaultMainMenu()
    print("Here are your passwords!\n")
    count = 1
    for password in passwordSets:
        print(f"#{count}: Site: {password[0]}, Username: {password[1]}, Password: {password[2]}")
        count += 1
    input("\nPress enter to continue...")

def insertPasswordMenu():
    os.system('clear')
    print("please insert the following information:")
    site = input("(OPTIONAL) From which site is this password? ")
    user = input("What is your username? ")
    password = input("What is your password? ")
    print(f"""
    Site: {site}
    User: {user}
    Password: {password} 
    """)
    selection = input("Is this correct? (y/n): ")
    if(selection == 'n'):
        ...
    elif(selection == 'y'):
        string = site+"-"+user+"-"+password
        cryptMan.encrypt_and_register_Pass(string)

def deletePasswordMenu():
    listPasswordMenu()
    index = int(input("Please select the index that will be deleted: "))
    fileMan.deletePassword(index)