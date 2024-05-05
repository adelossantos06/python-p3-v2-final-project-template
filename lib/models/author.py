from __init__ import CURSOR, CONN

class Author:

    all = []
    
    def __init__(self, name, age, genre):
        self._name = name
        self._age = age
        self._genre = genre

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

    @genre.setter
    def genre(self, genre):
        if type(genre) == str and len(genre) > 1:
            self._genre = genre
        else:
            raise  ValueError("Enter a valid genre")

    @classmethod
    def get_all_authors(cls):
        return Author.all

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Genre: {self.genre}"

# king = Author("Stephen King", 76, "horror")


# print(author.name)
# print(author.age)
# print(author.genre)
# print(author)
# print(Author.all)

# print(Author.get_all_authors())

 
