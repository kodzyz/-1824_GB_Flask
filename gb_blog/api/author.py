from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_blog.extensions import db
from gb_blog.models import Author
from gb_blog.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
