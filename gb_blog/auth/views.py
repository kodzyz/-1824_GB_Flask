from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, url_prefix="/auth", static_folder='../static')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        # то рисуем шаблон
        return render_template(
            'auth/login.html',
        )
    # elif request.method == 'POST':
    # получаем данные из формы
    # <input type="text" class="form-control" name="email">
    from gb_blog.models import User
    email = request.form.get('email')
    # print(email)
    #  <input type="password" class="form-control" name="password">
    password = request.form.get('password')
    # print(password)

    # найдем пользователя по 'email'
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
