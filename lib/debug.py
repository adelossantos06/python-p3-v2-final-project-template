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

# king = Author("Stephen King", 76)

# print(king)


# king.save()

# print(king)


# picoult = Author.create("Jodi Picoult", 46)


# rowling = Author.create("J.K. Rowling", 58)

# rowling.name = "JK Rowling"
# rowling.age = 60
# rowling.update()

# owens = Author.create("Delia Owens", 75)
# owens.delete()

# book_one = Book.create("IT", 856, "horror", "Stephen King")
# print(book_one)

picoult = Author.create("Jodi Picoult", 46)
king = Author.create("Stephen King", 75)
book_one = Book.create("Mad Honey", 456, "saga", picoult.id)
book_two = Book.create("Small Great Things", 574, "saga", picoult.id)
book_three = Book.create("IT", 856, "horror", king.id)



ipdb.set_trace()
