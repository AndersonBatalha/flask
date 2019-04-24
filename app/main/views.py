from flask import render_template, request, session, url_for, redirect, flash
from flask_login import login_required
from . import main
from .forms import NameForm

@main.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        nome_anterior = session.get('name')
        if nome_anterior is not None and nome_anterior != form.name.data:
            flash('Parece que você alterou o nome!')
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'))

@main.route('/user/<name>')
@login_required
def user(name):
    return render_template('user.html', name=name)

@main.route('/navegador')
def navegador():
    user_agent = request.headers.get('User-Agent')
    return "<p>Seu navegador: %s.</p>" %(user_agent)

@main.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404