class Book:
    def __init__(self, title, author, year):
        '''
        Initialize a Book object.
        '''
        self.title = title
        self.author = author
        self.year = year
        
    def show_info(self):
        '''
        This method prints out the book's title, author, and year of publication.
        '''
        return f"'{self.title}' by {self.author} ({self.year})"


class EBook(Book):
    def __init__(self, title, author, year,mb):
        super().__init__(title, author, year)
        self.mb = mb  

    def show_info(self):
        '''
        This method prints out the book's title, author, year of publication, and size of the file.
        '''
        return super().show_info()+f" size: {self.mb} MB"


class Library:
    def __init__(self):
        self.book_collection = []
    
    def add_book(self,book):
        '''
        This method adds a book to the library collection.
        '''
        self.book_collection.append(book)
        print(f"{book.title} added successfully!")
    
    def search_book(self,title):
        '''
        This method searches for a book by title in the library collection.
        '''
        for book in self.book_collection:
            if book.title.lower() == title.lower():
                print(f"{title} found!")
                return book
        print(f"{title} not found!")
        return None
        
    def remove_book(self,title):
        '''
        This method removes a book from the library collection.
        '''
        for book in self.book_collection:
            if book.title.lower() == title.lower():
                self.book_collection.remove(book)
                print(f"{book.title} removed successfully!")
                return
        print(f"{title} not found!")
        
    def display_books(self)-> None:
        '''
        This method prints the books stored in the Library object.
        '''
        if not self.book_collection:
            print("No books found, library is empty!")
            
        else:
            print()
            print("Availabe Books".center(50,'*'))
            for books in self.book_collection:
                print(books.show_info().center(50,' '))        

def get_book_info_from_user():
    '''
    This function asks the user which operation to perfom. The user gives the input required to perform the operations.
    '''
    book_type = input("Enter book type (book/ebook):").strip().lower()
    title = input("Enter book title:").strip()
    author = input("Enter book author:").strip()
    year = int(input("Enter published year:").strip())
    
    if book_type == "ebook":
        file_size = float(input("Enter the file size of ebook:").strip())
        return EBook(title, author, year, file_size)
    elif book_type == "book":
        return Book(title, author, year)
    else:
        print("Invalid book type, please enter either book or ebook.")

#PROGRAM EXECUTION BEGINS FROM HERE.        
my_library = Library()
while True:
    print("\n1. Add Book\n2. Display All\n3. Search Book\n4. Remove Book\n5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        book_obj = get_book_info_from_user()
        my_library.add_book(book_obj)

    elif choice == "2":
        my_library.display_books()

    elif choice == "3":
        title = input("Enter title to search: ").strip()
        my_library.search_book(title)

    elif choice == "4":
        title = input("Enter title to remove: ").strip()
        my_library.remove_book(title)

    elif choice == "5":
        print("Exiting now")
        break

    else:
        print("Invalid choice. Try again.")

# b1 = Book('Harry Potter','J.K Rowling',1999)
# b2 = Book('Spider-Man','Stan Lee',1995)
# ebook1 = EBook("Python Programming", "John Zelle", 2017,5)


# my_library.add_book(b1)
# my_library.add_book(b2)
# my_library.add_book(ebook1)

# my_library.display_books()
# my_library.search_book("Spider-Man")

# my_library.remove_book("Spider-Man")
# my_library.remove_book("Bat-man")

# # my_library.remove_book("Python Programming")

# print("After removing some books")
# my_library.display_books()