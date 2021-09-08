from database.models.tables.book import Book


def create_book(name, author, rating):
    return Book.create(name=name, author=author, rating=rating)


def get_all_books():
    return Book.get_all_books()
