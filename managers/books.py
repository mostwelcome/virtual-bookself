from database.models.tables.book import Book


def create_book(name, author, rating):
    return Book.create(name=name, author=author, rating=rating)


def get_all_books():
    return Book.get_all_books()


   
def update_book_rating(id, rating):
    book_to_update = Book.get_book(id=id)
    book_to_update.rating = rating
    book_to_update.save()

def get_book_details_by_id(id):
    return Book.get_book(id=id)


def delete_book_details(id):
    book_to_delete = Book.get_book(id=id)
    return Book.delete_book(book_to_delete)