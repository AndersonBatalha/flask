from . import auth
from flask import render_template, url_for, flash, redirect
from flask_login import login_user
from .forms import LoginForm
from app.models import User

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(username=form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            if next is None or not next.starswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)