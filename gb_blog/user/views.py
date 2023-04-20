from flask import Blueprint, render_template, redirect
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
    return render_template(
        'users/list.html',
        users=USERS,
    )


@user.route('/<int:pk>')  # http://127.0.0.1:8000/users/123
def get_user(pk: int):
    try:
        user_context = USERS[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect('/users/')
    return render_template(
        'users/details.html',
        user_context=user_context,
    )
