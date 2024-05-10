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






def exit_program():
    print("Goodbye!")
    exit()
