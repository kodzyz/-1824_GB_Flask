from flask_combo_jsonapi import ResourceList, ResourceDetail
from gb_blog.api.permissions.user import UserListPermission, UserPatchPermission
from gb_blog.extensions import db
from gb_blog.models import User
from gb_blog.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserListPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_patch': [UserPatchPermission],
    }
