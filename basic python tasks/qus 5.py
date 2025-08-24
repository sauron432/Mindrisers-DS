print("Enter text to insert into the file:")
print("Enter 'exit' or 'EXIT' to exit.")
while True:
    user_input = input("->").strip()
    with open('Input log.txt','a') as file:
        if user_input.lower().strip() == 'exit':
            print('Now exiting the program!!!')
            break
        file.writelines(user_input+'\n')
            