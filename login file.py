def register():
    username = input("Enter your username:").casefold().strip()       
    password = input("Password:").strip()
    
    with open("userdata.txt","a+") as file:    
        file.seek(0)
        content = file.read()
        usernames_in_file = [name.strip() for name in content.split(',') if name.strip()]
        if username in usernames_in_file:
            print("User already exists!")
        else:
            file.write(username + ",")
            print("Registration successful! Ridirecting to login section")
    login()
    
    
def login():
    username = input("Username:").casefold().strip()
    password = input("Password:").strip()
    with open("userdata.txt","r") as file:
        content = file.read()
        usernames_in_file = [name.strip() for name in content.split(',') if name.strip()]
        if username in usernames_in_file:
            print("Login successful!")
        else:
            print("User does not exist! You will now be redirected to the registration section.")
            register()
            
    
choice = input("What opertaion do u want to perform? Choose  'l' for login and 'r' for new register:").lower()

match choice:
    case 'l':
        login()
    case 'r':
        register()
    case _:
        print("Invalid choice. Please choose 'l' for login and 'r' for new register")