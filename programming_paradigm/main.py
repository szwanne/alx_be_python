from library_management import Book, Library
import sys
from robust_division_calculator import safe_divide


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    try:
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])
    except ValueError:
        print("Error: Please provide valid numbers.")
        sys.exit(1)

    result = safe_divide(numerator, denominator)
    if result is not None:
        print(f"The result of the division is {result:.1f}")


if __name__ == "__main__":
    main()


def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
