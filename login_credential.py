import json 
import getpass
def register():
    username = input("Input your username:").lower().strip()
    password = getpass.getpass("Input your password:").strip()
    user_credential = {username:password}
    json_credential = json.dumps(user_credential)
    
    with open("user_credentials.txt", "a") as file:
        file.write(json_credential + '\n')

def login():
    username = input("Enter your username:").lower().strip()
    password = getpass.getpass("Input your password:").strip()
    with open("user_credentials.txt", "r") as file:
        content = file.read()
        usernames_in_file = [i for i in content.split('\n') if i.strip()]
        # print(usernames_in_file)
        for i in usernames_in_file:
            dict_i = json.loads(i)
            if username in dict_i and dict_i[username]==password:
                print("Login Successful.")
                break
        else:
            print("Invalid credential!. Please try again")
            
choice = input("What opertaion do u want to perform? Choose  'l' for login and 'r' for new register:").lower()
match choice:
    case 'l':
        login()
    case 'r':
        register()
    case _:
        print("Invalid choice. Please choose 'l' for login and 'r' for new register")