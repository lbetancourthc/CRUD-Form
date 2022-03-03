from files import *
from user import *

def menu():
    flag = True
    while(flag):
        option_flag = False
        while(not option_flag):
            print("\n=============== MAIN MENU ===============")
            print("|                                        |")
            print("|    1. Register users                   |")
            print("|    2. List users                       |")
            print("|    3. Update users                     |")
            print("|    4. Delete users                     |")
            print("|    5. Exit                             |")
            print("|________________________________________|\n")

            option = int(input("Select an option: "))

            if option < 1 or option > 5:
                print("\nWrong option, enter again...\n")
            
            elif option == 1:
                User.registerUser()
                User.saveNewUser()
            
            elif option == 2:
                User.listUsers()
            
            elif option==3:
                User.updateUser()

            elif option==4:
                User.deleteUser()
            
            elif option == 5:
                print("Bye....")
                flag = False
                break
            else:
                option_flag = True
                pass



if __name__ == "__main__":
    
    Files.chechkJSON('data.json')
    menu()