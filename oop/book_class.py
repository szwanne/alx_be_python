class Book:
    """
    A class to model a book with a title, author, and publication year.
    It includes several magic methods to enhance its functionality.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize the book's title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the book object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
