import os
import click
# Book class to represent a book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price:.2f}"

# BookStore class to manage the book store
class BookStore:
    def __init__(self, file_name):
        self.file_name = file_name
        self.books = self.load_books()

    def load_books(self):
        books = []
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                for line in f:
                    title, author, price = line.strip().split(",")
                    books.append(Book(title, author, float(price)))
        return books

    def save_books(self):
        with open(self.file_name, "w") as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.price:.2f}\n")

    def add_book(self, title, author, price):
        self.books.append(Book(title, author, price))
        self.save_books()

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        self.save_books()

    def list_books(self):
        for book in self.books:
            print(book)

    def search_books(self, query):
        results = [book for book in self.books if query in book.title or query in book.author]
        for book in results:
            print(book)


@click.group()
def cli():
    pass

@click.argument("title")
@click.argument("author")
@click.argument("price", type=float)
def add_book(title, author, price):
    book_store = BookStore("books.txt")
    book_store.add_book(title, author, price)
    click.echo(f"Added book: {title} by {author} ${price:.2f}")

@cli.command()

def remove_book(title):
    book_store = BookStore("books.txt")
    book_store.remove_book(title)
    click.echo(f"Removed book: {title}")

@cli.command()
def list_books():
    book_store = BookStore("books,txt")
    book_store.list_books()

@click.command()
@click.argument("query")
def search_books(query):
    book_store = BookStore("books.txt")
    book_store.search_books(query)
def main():
    book_store = BookStore("books.txt")

    while True:
        print("Book Store CLI")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Books")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            book_store.add_book(title, author, price)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            book_store.remove_book(title)
        elif choice == "3":
            book_store.list_books()
        elif choice == "4":
            query = input("Enter search query: ")
            book_store.search_books(query)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()