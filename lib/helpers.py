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
    space()
    name = input("Author's name: ")
    space()
    age = int(input("Author's age: "))
    new_author = Author(name = name, age = age)
    new_author.create(name, age)


def delete_author():
    authors = Author.get_all()
    choice = input("> ")


    author = authors[int(choice) -1]
   
    for book in author.books():
        book.delete()
        
    author.delete()
    print("Author and their books removed successfully!")
    
   

def update_author():
    space()
    print("Which author would you like to update?")
    authors = list_authors()
    update_choice = input("> ")
    update_author = authors[int(update_choice) -1]
    space()
    name_or_age = input("Would like to update the author name or age? ")
    space()
    if name_or_age == "name":
        space()
        new_name = input("Update author name: ")
        update_author.name = new_name
    elif name_or_age == "age":
        space()
        new_age = input("Update author age: ")
        update_author.age = new_age
    else:
        space()
        print("Invalid input")
        space()
    update_author.update()
    space()
    print("Author updated sucessfully!")
    space()

def list_all_books():
    books = Book.get_all()
    
    for i, book in enumerate(books, start=1):
        author = book.author()
        author_name = author.name if author else "Unknown" 
        print(f"{i}. Title: {book.title}, Page count: {book.page_count}, Genre: {book.genre}, Author: {author_name}")
    return books

    if not books:
        print("There are no books to list.")

def list_books_by_author(author):
    space()
    books = author.books()
    if books:
        for i, book in enumerate(books, start=1):

            print(f"{i}. Title: {book.title}, Page Count: {book.page_count}, Genre: {book.genre}")
        space()
        return books
    else:
        space()
        print("There are no books by this author.")
    space()
  


def add_book_by_author(author):
    space()
    title = input("Book's title: ")
    page_count = int(input("Book's page count: "))
    genre = input("Book's genre: ")
    space()
    new_book= Book(title = title, page_count = page_count, genre = genre, author_id=author.id)
    new_book.create(title, page_count, genre, author.id)
    print("Book added successfully!")
    space()

def delete_book_by_author(author):
    books = list_books_by_author(author)
    print("Which book would you like to delete?")
    choice = input("> ")
    book = books[int(choice) -1]
    book.delete()
    print("Book deleted successfully!")
    space()
    
    

def update_book_by_author(author):
    space()
    print("Which book would you like to update: ")
    books = list_books_by_author(author)
    
    choice = input("> ")
    update_book = books[int(choice) -1]
    space()
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
        space()
        print("Invalid input")
        space()
        return

    update_book.update()
    space()
    print("Book updated sucessfully!")
    space()

def space():
    print(" ")

def exit_program():
    print("Goodbye!")
    exit()
