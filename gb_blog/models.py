from flask_login import UserMixin

from gb_blog.app import db


class User(db.Model, UserMixin):
    # __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    about = db.Column(db.Text())
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, about, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.email = email
        self.password = password



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

