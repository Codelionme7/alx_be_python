# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize the book with title, author, and private availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty private list of books."""
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                break 

    def return_book(self, title):
        """Find a book by title and return it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                break

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")