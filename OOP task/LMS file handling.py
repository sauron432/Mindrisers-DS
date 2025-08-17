import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def show_info(self):
        return f"'{self.title}' by {self.author} ({self.year})"
        
class EBook(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)
        # self.mb = mb 
        
    def show_info(self):
        return super().show_info() 

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.book_collection = []
        self.load_books()
    
    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                book_data = json.load(f)
                for book_dict in book_data:
                    self.book_collection.append(Book(**book_dict))
            print("Library data loaded successfully.")
        except FileNotFoundError:
            print("No existing library file found. Starting with an empty library.")
        
    def save_books(self):
        # Prepare the data for JSON serialization
        book_data = []
        for book in self.book_collection:
            book_data.append(book.__dict__)
        
        with open(self.filename, 'w') as f:
            json.dump(book_data, f,indent=4)
        print("Library data saved successfully.")
        
    def add_book(self, book):
        self.book_collection.append(book)
        self.save_books()
        print(f"'{book.title}' added successfully!")

    def search_book(self, title):
        for book in self.book_collection:
            if book.title == title:
                print(f"'{title}' found!")
                return book
        print(f"'{title}' not found!")
        return None
        
    def remove_book(self, title):
        original_length = len(self.book_collection)
        self.book_collection = [
            book for book in self.book_collection
            if book.title.lower() != title.lower()
        ]
        
        if len(self.book_collection) < original_length:
            self.save_books()
            print(f"'{title}' removed successfully!")
        else:
            print(f"'{title}' not found!")
            
    def display_books(self):
        if not self.book_collection:
            print("No books found, library is empty!")
        else:
            print("Available Books".center(50, '*'))
            for book in self.book_collection:
                print(book.show_info().center(50, ' '))
my_library = Library()

b1 = Book('Harry Potter', 'J.K Rowling', 1999)
b2 = Book('Spider-Man', 'Stan Lee', 1995)
ebook1 = EBook("Python Programming", "John Zelle", 2017)

my_library.add_book(b1)
my_library.add_book(b2)
my_library.add_book(ebook1)

my_library.display_books()

my_library.remove_book("Spider-Man")
my_library.remove_book("Super Man")

print("\n" + "After removing some books".center(50, '-'))
my_library.display_books()

