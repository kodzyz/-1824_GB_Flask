from flask_login import UserMixin

from gb_blog.app import db


class User(db.Model, UserMixin):
    # __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    about = db.Column(db.Text())
    email = db.Column(db.String(255), unique=True)
    age = db.Column(db.Integer)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, about, email, age, password, is_staff):
        self.name = name
        self.about = about
        self.email = email
        self.age = age
        self.password = password
        self.is_staff = is_staff


class Article(db.Model):
    # __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    author = db.Column(db.String(255))

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

