from app import db
from . import auth
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegisterForm
from app.models import User


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        flash("Usuário registrado!")

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.starswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

@login_required
@auth.route('/logout')
def logout():
    logout_user()
    flash("A sessão atual foi encerrada")
    return redirect(url_for('main.index'))


