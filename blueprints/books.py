from flask import Blueprint, request, render_template, redirect, url_for, flash, session

from managers.books import get_all_books, create_book
BOOKS_BLUEPRINT = Blueprint('books', __name__)


@BOOKS_BLUEPRINT.route('/')
def books_list():
    all_books = get_all_books()
    book_list = []
    for book in all_books:
        book_list.append({
            'name':book.name,
            'author':book.author,
            'rating':book.rating
        })
    context = {
        'books': book_list
    }
    # return render_template('index.html', **context)
    return context


@BOOKS_BLUEPRINT.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        new_book = create_book(name='abc5', author='ttt', rating=2)
        return redirect(url_for('home'))
    return render_template('add_book.html')