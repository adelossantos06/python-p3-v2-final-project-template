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
        print("There are no authors.")
        space()



def add_authors():
    space()
    name = input("Author's name: ")
    space()
    age = int(input("Author's age: "))
    Author.create(name = name, age = age)
    space()
    print("Author added successfully!")



def delete_author():
    authors = list_authors()
    if not authors:
        return
    space()
    print("Which author would you like to delete?")
    choice = int(input("> "))
    space()
    if choice > len(authors):
        print("Invalid input")
    else:
        author = authors[int(choice) -1]
        for book in author.books():
            book.delete()
        author.delete()
        space()
        print("Author and their books removed successfully!")
    
   

def update_author():
    space()
    authors = list_authors()
    
    if not authors: 
        return
    print("Which author would you like to update?")
    space()
    choice = int(input("> "))
    space()
    if choice > len(authors):
        print("Invalid input")
        space()
    else:
        author = authors[int(choice) -1]
        space()
        name_or_age = input("Would like to update the author name or age? ")
        space()
        if name_or_age == "name":
            space()
            new_name = input("Update author name: ")
            author.name = new_name
            space()
            print("Author updated sucessfully!")
        elif name_or_age == "age":
            space()
            new_age = input("Update author age: ")
            author.age = new_age
            space()
            print("Author updated sucessfully!")
        else:   
            space()
            print("Invalid input")
            space()
        author.update()
   



def list_all_books():
    books = Book.get_all()
    if books:
        for i, book in enumerate(books, start=1):
            author = book.author()
            author_name = author.name if author else "Unknown" 
            print(f"{i}. Title: {book.title}, Page count: {book.page_count}, Genre: {book.genre}, Author: {author_name}")
        return books
    else:
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
    Book.create(title = title, page_count = page_count, genre = genre, author_id=author.id)
    print("Book added successfully!")
    space()



def delete_book_by_author(author):
    books = list_books_by_author(author)
    if not books:
        return
    space()
    print("Which book would you like to delete?")
    choice = input("> ")
    book = books[int(choice) -1]
    book.delete()
    space()
    print("Book deleted successfully!")
    space()
    
    

def update_book_by_author(author):
    space()
    print("Which book would you like to update: ")
    books = list_books_by_author(author)
    
    if not books:
        return
    space()
    choice = int(input("> "))
    if choice < 1 or choice > len(books):
        print("Invalid input")
        space()
        return
    book = books[choice -1]

    update_choice = input("Do you want to update the title, page count or genre? ")

    if update_choice == "title":
        new_title = input("Update the title: ")
        book.title = new_title
    elif update_choice == "page count":
        new_page_count = input("Update the page count: ")
        book.page_count = new_page_count
    elif update_choice == "genre":
        new_genre = input("Update the book genre: ")
        book.genre = new_genre
    else:
        space()
        print("Invalid input")
        space()
        return
    book.update()
    space()
    print("Book updated sucessfully!")
    space()

def add_book_bookmenu(author):
    space()
    print("Select an author to add a book: ")
    authors = list_authors()
    space()
    choice = int(input("> "))
    if choice > len(authors):
        space()
        print("Invlid input")
        return
    author = authors[int(choice) -1]

    if choice:
        add_book_by_author(author)
    else:
        print("Invalid input")

def update_book_bookmenu(author):
    space()
    print("Select an author to update a book: ")
    authors = list_authors()
    space()
    choice = int(input("> "))
    if choice > len(authors):
        space()
        print("Invlid input")
        return
    author = authors[int(choice) -1]

    if choice:
        update_book_by_author(author)
    else:
        print("Invalid input")


def delete_book_bookmenu(author):
    space()
    print("Select an author to delete a book: ")
    authors = list_authors()
    space()
    choice = int(input("> "))
    if choice > len(authors):
        space()
        print("Invlid input")
        return
    author = authors[int(choice) -1]

    if choice:
        delete_book_by_author(author)
    else:
        print("Invalid input")

def space():
    print(" ")

def exit_program():
    space()
    print("Goodbye!")
    space()
    exit()
