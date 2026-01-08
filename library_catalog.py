"""Library Catalog Management System"""

# List to store book information
library_catalog = [
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
]


# Function to display all books in the catalog
def display_books():
    """Displays all books in the library catalog."""
    print("Library Catalog:")
    for book_title, book_author, year_written in library_catalog:
        print(f"Title: {book_title}, Author: {book_author}, Year: {year_written}")


# Function to add a new book to the catalog
def add_book(book_title, book_author, year_written):
    """Adds a new book to the library catalog."""
    new_book = (book_title, book_author, year_written)
    library_catalog.append(new_book)
    print(f"Book '{book_title}' by {book_author} added to the catalog.")


# Function to search for books by an author
def search_by_author(book_author):
    """Searches for books by the given author."""
    books_by_author = []
    for book in library_catalog:
        _, current_author, _ = book
        if current_author.lower() == book_author.lower():
            books_by_author.append(book)
    return books_by_author


# Displaying the books
display_books()

# Adding a new book
add_book("The Catcher in the Rye", "J.D. Salinger", 1951)

# Displaying the books again
display_books()

# Searching for books by George Orwell
books_by_orwell = search_by_author("George Orwell")
print("Books by George Orwell:")
for title, author, year in books_by_orwell:
    print(f"Title: {title}, Year: {year}")
