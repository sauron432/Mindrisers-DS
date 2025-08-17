# TASK:
# Implement all the three operations of file handling

file = open('newfile.txt','w')

file.writelines(["We have successfully created a file.",
                 "\nWe will now write into the file using file handling.",
                 "\nThe 'writelines()' method writes multiple lines into the file",
                 "\nIt takes a list of strings as an input.",
                 "\nIt does not include line breaks so we will add it manually."])
print("You have created and written into the file.")
file.close()

file = open('newfile.txt','r')
file_content = file.read()

print("File content:\n",file_content)

file.close()

file = open('newfile.txt','a+')
file.write("\nThis is an additional line of text wich is appended into the file using append mode.")

file.seek(0) # Moves the cursor to the start of file as in append mode, the cursor is at EOF by default.
new_file = file.read()
print("\nFile content after appending a new line:\n",new_file)

type(new_file)
file.close()