from models.__init__ import CURSOR, CONN
from models.book import Book

class Author:
    
    def __init__(self, name, age, id=None):
        self.name = name
        self.age = age
        self.id = id

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
         self._name = name
        
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    def __repr__(self):
       return f"Id:{self.id}  Name: {self.name}, Age: {self.age}"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS authors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO authors (name, age)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, age):
        author = cls(name, age)
        author.save()
        return author

    def update(self):
        sql = """
            UPDATE authors
            SET name = ?, age = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        return cls(row[1], row[2],row[0])


    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row)for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM authors
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def books(self):


        sql = """
            SELECT * FROM books
            WHERE author_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Book.instance_from_db(row) for row in rows]