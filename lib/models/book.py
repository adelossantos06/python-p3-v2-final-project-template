from models.__init__ import CURSOR, CONN

class Book:
    
    def __init__(self, title, page_count, genre, author_id, id=None):
        self.title = title
        self.page_count = page_count
        self.genre = genre
        self.author_id = author_id
        self.id = id


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        self._title = title

    @property
    def page_count(self):
        return self._page_count
    

    @page_count.setter
    def page_count(self, page_count):
        if not isinstance(page_count, int):
            raise ValueError("Page count must be a positive integer")
        self._page_count = page_count
       
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str):
            raise ValueError("Genre must be a non-empty string.")
        self._genre = genre


    def __repr__(self):
       return f"Id:{self.id}, Title: {self.title},  page_count: {self.page_count}, Genre: {self.genre}, Author: {self.author_id}"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                page_count INTEGER,
                genre TEXT,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod  
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO books (title, page_count, genre, author_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.page_count, self.genre, self.author_id))
        CONN.commit()

        self.id = CURSOR.lastrowid


    @classmethod
    def create(cls, title, page_count, genre, author_id):
        book = cls(title, page_count, genre, author_id)
        book.save()
        return book

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, page_count = ?, genre = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.page_count, self.genre, self.author_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        return cls(row[1], row[2], row[3], row[4], row[0])
    

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row)for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM books
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def author(self):
        from models.author import Author
        sql = """
            SELECT * FROM authors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (self.author_id,)).fetchone()
        return Author.instance_from_db(row) if row else None