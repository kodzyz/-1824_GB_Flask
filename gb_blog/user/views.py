from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: {
        'name': 'Нуцубидзе Альфред',
        'about': 'Россия, г.Волгоград, 38 лет',
    },
    2: {
        'name': 'Дмитрий Кокшаров',
        'about': 'Доктор технических наук, доцент, главный научный сотрудник Института проблем управления Российской Академии наук',
    },

    3: {
        'name': 'Алиева Бронислава',
        'about': 'Senior Python Developer в Б-152',
    },
}


@user.route('/')  # http://127.0.0.1:8000/users/
def user_list():
    from gb_blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')  # http://127.0.0.1:8000/users/123
@login_required
def profile(pk: int):
    from gb_blog.models import User
    _user = User.query.filter_by(id=pk).one_or_none()
    if _user is None:
        raise NotFound(f"User id:{pk}, not found")
    return render_template(
        'users/profile.html',
        user=_user,
    )
