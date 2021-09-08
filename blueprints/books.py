from database.models.tables.book import Book
from flask import Blueprint, request, render_template, redirect, url_for, flash, session

from managers.books import get_all_books, create_book, get_book_details_by_id, update_book_rating
BOOKS_BLUEPRINT = Blueprint('books', __name__)


@BOOKS_BLUEPRINT.route('/')
def books_list():
    all_books = get_all_books()
    book_list = []
    for book in all_books:
        book_list.append({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'rating': book.rating
        })
    context = {
        'books': book_list
    }
    return render_template('index.html', **context)
    # Can return context json
    # return context


@BOOKS_BLUEPRINT.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = create_book(
            name=request.form['name'], author=request.form['author'], rating=request.form['rating'])
        return redirect(url_for('home'))
    return render_template('add_book.html')


@BOOKS_BLUEPRINT.route('/edit/<id>', methods=['POST', 'GET'])
def edit_rating(id=None):
    if request.method == 'GET':
        book_to_update = get_book_details_by_id(id)
        context = {
            'book': book_to_update
        }
        return render_template('edit_rating.html', **context)
    elif request.method == 'POST':
        update_book_rating(id, request.form['rating'])
        return redirect(url_for('books.books_list'))
