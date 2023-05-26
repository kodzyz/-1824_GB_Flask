from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound
from gb_blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')  # http://127.0.0.1:8000/users/
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')  # http://127.0.0.1:8000/users/123
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if selected_user is None:
        raise NotFound(f"User id:{pk}, not found")
    return render_template(
        'users/profile.html',
        user=selected_user,
    )
