# Base class for a Book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"'{self.title}' by {self.author} ({self.year})"


# Derived class for an EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)  # Inherit attributes from Book
        self.file_size_mb = file_size_mb

    def display_info(self):
        return super().display_info() + f" [E-Book, {self.file_size_mb}MB]"


# Library class to manage books
class Library:
    def __init__(self):
        self.books = []  # Store Book and EBook objects

    def add_book(self, book):
        self.books.append(book)
        print(f" Book added: {book.display_info()}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book removed: {book.display_info()}")
                return
        print(f" Book '{title}' not found in the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book.display_info()}")
                return book
        print(f"Book '{title}' not found.")
        return None

    def display_all_books(self):
        if not self.books:
            print(" No books in the library.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(f" - {book.display_info()}")


# ----------- Example Usage -----------

# Create library
my_library = Library()

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
ebook1 = EBook("Python Programming", "John Zelle", 2017, 5)

# Add books
my_library.add_book(book1)
my_library.add_book(ebook1)

# Display all
my_library.display_all_books()

# Search for a book
my_library.search_book("The Great Gatsby")

# Remove a book
my_library.remove_book("Python Programming")

# Try removing again (should show not found)
my_library.remove_book("Python Programming")

# Display after removal
my_library.display_all_books()
