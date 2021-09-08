from flask import Flask, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from blueprints.books import BOOKS_BLUEPRINT


app = Flask(__name__)
app.config.from_pyfile('config/settings.staging.cfg')
db = SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(BOOKS_BLUEPRINT, url_prefix='/books')


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return redirect(url_for('books.books_list'))


if __name__ == '__main__':
    app.run()
