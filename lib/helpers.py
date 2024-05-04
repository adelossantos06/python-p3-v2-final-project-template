# lib/helpers.py
from models.author import Author
from models.book import Book

def list_authors():
    authors = Author.get_all()
    for author in authors:
        print(author)

def helper_11():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
