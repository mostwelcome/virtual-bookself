from database.db import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __str__(self) -> str:
        return f'{self.name}'

    @classmethod
    def create(cls, **kwargs):
        book = cls(**kwargs)
        return book.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_all_books(cls):
        return cls.query.all()

    @classmethod
    def get_book(cls, id):
        return cls.query.get(id)
 