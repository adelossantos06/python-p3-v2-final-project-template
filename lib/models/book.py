from models.__init__ import CURSOR, CONN
# from models.author import Author

class Book:

    all = {}
    
    def __init__(self, title, page_count, genre, author_id, id=None):
        self._title = title
        self._page_count = page_count
        self._genre = genre
        self.author_id = author_id
        self.id = id


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
    
    # @page_count.setter
    # def page_count(self, page_count):
    #     if isinstance(page_count, int):
    #         self._page_count = page_count
    #     else:
    #         raise ValueError ("Enter valid page count. ")

    @page_count.setter
    def page_count(self, page_count):
            self._page_count = page_count
       
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if type(genre) == str and len(genre) > 1:
            self._genre = genre
        else:
            raise ValueError("Enter a valid book genre")

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

        Book.all[self.id] = self

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

        del Book.all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])

        if book:
            book.title = row[1]
            book.page_count = row[2]
            book.genre = row[3]
            book.author_id = row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
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
        author = Author.instance_from_db(row)
        return author