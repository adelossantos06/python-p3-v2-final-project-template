# from models.__init__ import CURSOR, CONN
# from models.author import Author

class Book:

    all = []
    
    def __init__(self, title, author, page_count, genre):
        self._title = title
        self._author = author
        self._page_count = page_count
        self.genre = genre

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
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if type(author) == str and len(author) > 1:
            self._author = author
        else:
            raise ValueError("Enter valid book author")

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
    
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, page_count: {self.page_count}, Genere: {self.genre}"

king_book = Book("11/22/63", "Stephen King", 849, "science fiction")

Book.all.append(king_book)

print(king_book.title)
print(king_book.author)
print(king_book.page_count)
print(king_book)

print(Book.all)