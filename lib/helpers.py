# lib/helpers.py
from models.author import Author
from models.book import Book



def list_authors():
    print ("0. Go back to the main menu")
    authors = Author.get_all()
    for author in authors:
        print( f"{author.id}. {author.name}")



def exit_program():
    print("Goodbye!")
    exit()
