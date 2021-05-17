import datetime
import pickle


class Book:
    ISBN: int
    name: str
    author: str
    publisher: str
    publish_date: datetime.date

    def __init__(self, ISBN, name, author, publisher, publish_date):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date

    @classmethod
    def unpickle_file(cls):
        cls.book_list = pickle.load(open("books.pkl"))
        return cls.book_list


books = Book.unpickle_file()
print(books)
