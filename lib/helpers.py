# lib/helpers.py
from models.author import Author
from models.book import Book



def list_authors():
    authors = Author.get_all()
    if authors:
        for i, author in enumerate(authors, start=1):
            print(f"{i}. {author.name}")
        return authors
    else:
        print("There are no authors to list.")

def add_authors():
    print("***")
    name = input("Author's name: ")
    print("***")
    age = int(input("Author's age: "))
    new_author = Author(name = name, age = age)
    new_author.create(name, age)

def delete_author():
    authors = list_authors()
    delete_choice = input("> ")
    delete_author = authors[int(delete_choice) -1]
    delete_author.delete()
    print("Author deleted successfully!")

def update_author():
    print("***")
    print("Which author would you like to update?")
    authors = list_authors()
    update_choice = input("> ")
    update_author = authors[int(update_choice) -1]
    print("***")
    name_or_age = input("Would like to update the author name or age? ")
    print("***")
    if name_or_age == "name":
        print("***")
        new_name = input("Update author name: ")
        update_author.name = new_name
    elif name_or_age == "age":
        print("***")
        new_age = input("Update author age: ")
        update_author.age = new_age
    else:
        print("***")
        print("Invalid input")
        print("***")
    update_author.update()
    print("***")
    print("Author updated sucessfully!")
    print("***")

def list_all_books():
    books = Book.get_all()
    
    for i, book in enumerate(books, start=1):
        author = book.author()
        author_name = author.name if author else "Unknown" 
        print(f"{i}. Title: {book.title}, Page count: {book.page_count}, Genre: {book.genre}, Author: {author_name}")

    if not books:
        print("There are no books to list.")

def list_books_by_author(author):
    books = Book.get_all()

    author_books = [book for book in books if book.author_id == author.id]

    if author_books:
        for i, book in enumerate(author_books, start=1):
            print(f"{i}. Title: {book.title}, Page Count: {book.page_count}, Genre: {book.genre}")
        return author_books
    else:
        print("***")
        print("There are no books by this author.")
  


def add_book_by_author(author):
    print("***")
    title = input("Book's title: ")
    page_count = int(input("Book's page count: "))
    genre = input("Book's genre: ")
    print("***")
    new_book= Book(title = title, page_count = page_count, genre = genre, author_id=author.id)
    new_book.create(title, page_count, genre, author.id)
    print("Book added successfully!")

def delete_book_by_author(author):
    books = list_books_by_author(author)
    print("Which book would you like to delete?")
    choice = input("> ")
    delete_book = books[int(choice) -1]
    delete_book.delete()
    print("Book deleted successfully!")

def update_book_by_author():
    print("***")
    print("Which book would you like to update: ")
    books = list_all_books()
    choice = input("> ")
    update_book = books[int(choice) -1]
    print("***")
    update_choice = input("Do you want to update the title, page count or genre? ")

    if update_choice == "title":
        new_title = input("Update the title: ")
        update_book.title = new_title
    elif update_choice == "page count":
        new_page_count = input("Update the page count: ")
        update_book.page_count = new_page_count
    elif update_choice == "genre":
        new_genre = input("Update the book genre: ")
        update_book.genre = new_genre
    else:
        print("***")
        print("Invalid input")
        print("***")
        return
        
    update_book.update()
    print("***")
    print("Book updated sucessfully!")
    print("***")

def exit_program():
    print("Goodbye!")
    exit()
