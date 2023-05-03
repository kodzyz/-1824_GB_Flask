from flask_login import UserMixin

from gb_blog.app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    about = db.Column(db.Text())
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)
    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, first_name, last_name, about, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.about = about
        self.email = email
        self.password = password


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    author = relationship('Author', back_populates='articles')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')
