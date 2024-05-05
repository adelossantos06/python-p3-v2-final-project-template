from models.__init__ import CURSOR, CONN
from models.author import Author

class Book:

    all = []
    
    def __init__(self, title, page_count, genre, author, id=None):
        self._title = title
        self._page_count = page_count
        self._genre = genre
        self._author = author
        self._id = id

        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else:
            raise ValueError ("Enter valid book title. ")

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int and page_count > 0:
            self._page_count = page_count
        else:
            raise ValueError("Enter a valid page count")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if type(genre) == str and len(genre) > 1:
            self._genre = genre
        else:
            raise ValueError("Enter a valid book genre")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance class of Author")

    @classmethod
    def get_all_books(cls):
        return Book.all
    
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author.name}, page_count: {self.page_count}, Genre: {self.genre}"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                tilte TEXT,
                page_count INTEGER,
                genre TEXT,
                author TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

