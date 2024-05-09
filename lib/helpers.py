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
    name = input("Author's name: ")
    age = int(input("Author's age: "))
    new_author = Author(name = name, age = age)
    new_author.create(name, age)

def delete_author():
    authors = list_authors()
    delete_choice = input("> ")
    delete_author = authors[int(delete_choice) -1]
    delete_author.delete()
    print("Author deleted successfully!!")





def exit_program():
    print("Goodbye!")
    exit()
