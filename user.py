import json
import pandas as pd
from files import *

global dict_data, list_user
dict_data = dict()
list_user = list()

class User:
    def __init__(self):
        self.surname = ""
        self.lastname = ""
        self.age = ""
        self.email = ""

    def registerUser():
        "Register a new user"
        user = User()
        user.surname = input("Enter surname: ")
        user.lastname = input("Enter lastname: ")
        user.age = int(input("Enter age: "))
        user.email = input("Enter email: ")
        list_user.append(user)

    def saveNewUser():
        "Save the new user"
        with open('data.json') as json_file:
            list_user_surname = []
            list_user_lastname = []
            list_user_age = []
            list_user_email = []

            data_json = json.load(json_file)
                        
            if len(data_json) != 0:
                print(len(data_json['Surname']))
                for i in range(len(data_json['Surname'])):
                    list_user_surname.append(data_json['Surname'][i])
                    list_user_lastname.append(data_json['Lastname'][i])
                    list_user_age.append(data_json['Age'][i])
                    list_user_email.append(data_json['Email'][i])

            for user in list_user:
                list_user_surname.append(user.surname)
                list_user_lastname.append(user.lastname)
                list_user_age.append(user.age)
                list_user_email.append(user.email)
            
            dict_data['Surname'] = list_user_surname
            dict_data['Lastname'] = list_user_lastname
            dict_data['Age'] = list_user_age
            dict_data['Email'] = list_user_email
            Files.saveJSON('data.json', dict_data)
            list_user.clear()

    def listUsers():
        "List all users in JSON file"
        with open('data.json') as json_file:
            data_json = json.load(json_file)
            df = pd.DataFrame.from_dict(data_json, orient="index")
            print(df)

    def deleteUser():
        "Delete an user by index"
        index = int(input("Index to delete: "))

        try:
            with open('data.json') as json_file:
                data_json = json.load(json_file)
                del data_json['Surname'][index], data_json['Lastname'][index], data_json['Age'][index], data_json['Email'][index]
                Files.saveJSON('data.json', data_json)
        except:
            print("\nError, enter again")

    def updateUser():
        "Update an user by index"
        index = int(input("Index to modify: "))
        new_surname = input("Enter new surname: ")
        new_lastname = input("Enter new lastname: ")
        new_age = int(input("Enter new age: "))
        new_email = input("Enter new email: ")

        try:
            with open('data.json') as json_file:
                data_json = json.load(json_file)
                data_json['Surname'][index] = new_surname
                data_json['Lastname'][index] = new_lastname
                data_json['Age'][index] = new_age
                data_json['Email'][index] = new_email            
                Files.saveJSON('data.json', data_json)
        except:
            print("\nError, enter again")