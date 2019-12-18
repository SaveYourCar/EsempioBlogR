"""

In quest controller sono presenti le funzioni di login e logout.
Va implementato un controller per la registrazione.
Attualmente il login e consentito solo a un utente inserito in modo manuale all'interno del file config.py
quindi i post che verranno inserito saranno solo di tale utente

"""

from flask import Blueprint, session, redirect, request, render_template
from core.config import configuration_params as params
from core.data_access.postsDA import get_posts
from core.models.userModel import User
from core.config import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        user = User.query.filter_by(username=username).first()
        if (user and userpass == user.password_hash):
            # set the session variable
            session['user'] = username
            posts = get_posts()
            return render_template('dashboard.html', params=params, posts=posts)
    return render_template('login.html', params=params)


# da completare
@auth.route("/signup")
def signup():
    User()
    return ""


@auth.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')



"""

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page)
        if (username == params['admin_user'] and userpass == params['admin_password']):
            # set the session variable
            session['user'] = username
            posts = get_posts()
            return render_template('dashboard.html', params=params, posts=posts)
    return render_template('login.html', params=params)
"""