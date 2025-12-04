# main.py
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    # This happens automatically when you print the object
    print(my_book)

    # Demonstrating the __repr__ method
    # This happens when you explicitly call repr()
    print(repr(my_book))

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()