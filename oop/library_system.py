# Base Class: Book
class Book:
    def __init__(self, title, author):
        """
        Initialize a generic book with title and author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Return a string with common book information.
        """
        return f"Book: {self.title} by {self.author}"

    def get_details(self):
        """
        Returns common attributes of all books.
        Subclasses may override this.
        """
        return f"{self.title} by {self.author}"

# Derived Class: EBook


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook with title, author, and file size in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Return detailed info including inherited and unique attributes.
        """
        return f"EBook: {self.get_details()}, File Size: {self.file_size}KB"

# Derived Class: PrintBook


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook with title, author, and page count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Return detailed info including inherited and unique attributes.
        """
        return f"PrintBook: {self.get_details()}, Page Count: {self.page_count}"

# Composition Class: Library


class Library:
    def __init__(self):
        """
        Create an empty library to hold books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add any type of Book (Book, EBook, PrintBook) to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Print out the details of each book in the library.
        """
        for book in self.books:
            print(book)
