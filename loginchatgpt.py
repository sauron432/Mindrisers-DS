def login():
    username = input("Username: ").casefold().strip()
    try:
        with open("userdata.txt", "r") as file:
            content = file.read()
            usernames_in_file = [name.strip() for name in content.split(',') if name.strip()]
    except FileNotFoundError:
        usernames_in_file = []

    if username in usernames_in_file:
        print("Login successful!")
    else:
        print("User does not exist! Redirecting to register section:")
        register()


def register():
    username = input("Enter your username: ").casefold().strip()
    try:
        with open("userdata.txt", "r") as file:
            content = file.read()
            usernames_in_file = [name.strip() for name in content.split(',') if name.strip()]
    except FileNotFoundError:
        usernames_in_file = []

    if username in usernames_in_file:
        print("Username already exists!")
    else:
        with open("userdata.txt", "a") as file:
            file.write(username + ',')
        print("Registry successful. Redirecting to login section:")
        login()


choice = input("What operation do you want to perform? Choose 'l' for login and 'r' for register: ").lower()

match choice:
    case 'l':
        login()
    case 'r':
        register()
    case _:
        print("Invalid choice. Please choose 'l' for login and 'r' for register.")
