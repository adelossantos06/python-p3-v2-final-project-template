from models.__init__ import CURSOR, CONN

class Author:

    all = []
    
    def __init__(self, name, age, id=None):
        self._name = name
        self._age = age
        self.id = id
       
        
        Author.all.append(self)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 1:
            self._name = name
        else:
            raise  ValueError("Enter a valid author name")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def genre(self):
        return self._genre
    
    @classmethod
    def get_all_authors(cls):
        return Author.all

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
