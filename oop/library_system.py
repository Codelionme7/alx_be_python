# library_system.py

class Book:
    def __init__(self, title, author):
        """Base class for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for base Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class for EBooks.
        Calls base __init__ for title/author, then sets file_size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation specific to EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class for PrintBooks.
        Calls base __init__ for title/author, then sets page_count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation specific to PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library uses COMPOSITION: It HAS A list of books."""
        self.books = []

    def add_book(self, book):
        """Adds any type of Book instance to the list."""
        self.books.append(book)

    def list_books(self):
        """Loops through the list and prints each book's details."""
        for book in self.books:
            print(book)