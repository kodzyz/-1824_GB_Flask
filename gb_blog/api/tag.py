from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_blog.extensions import db
from gb_blog.models import Tag
from gb_blog.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }
