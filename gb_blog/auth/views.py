from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from gb_blog.extensions import db
from gb_blog.forms.user import UserRegisterForm, UserLoginForm
from gb_blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template(
        'auth/login.html',
        form=UserLoginForm(request.form)
    )


@auth.route('/login', methods=('POST',))
def login_post():
    form = UserLoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Check your login details')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''вьюха для формы регистрации'''
    # if current_user.is_authenticated:
    #     return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        # уникальность email
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('auth/register.html', form=form)

        _user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            about=form.about.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        # login_user(_user)

        return redirect(url_for('auth.login_post'))

    return render_template(
        'auth/register.html',
        form=form,
        errors=errors,
    )
