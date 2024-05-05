#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book

import ipdb

def reset_database():
    Author.drop_table()
    Author.create_table()

reset_database()


ipdb.set_trace()
