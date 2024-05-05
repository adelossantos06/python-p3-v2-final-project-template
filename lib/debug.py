#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book

import ipdb

def reset_database():
    Author.drop_table()
    Author.create_table()
    Book.drop_table()
    Book.create_table()

reset_database()

king = Author("Stephen King", 76)
book = Book("IT", 846, "horror", "Stephen King")
print(king)
print (book)

king.save()
book.save()
print(king)
print(book)

picoult = Author.create("Jodi Picoult", 46)
book_two = Book.create ("Mad Honey", 452, "saga", "Jodi Picoult")

rowling = Author.create("J.K. Rowling", 58)

rowling.name = "JK Rowling"
rowling.age = 60
rowling.update()

owens = Author.create("Delia Owens", 75)
owens.delete()
ipdb.set_trace()
