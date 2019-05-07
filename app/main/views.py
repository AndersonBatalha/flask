from flask import render_template, request, session, url_for, redirect, flash
from flask_login import login_required

from app.models import Role, User
from . import main
from .forms import NameForm, RoleForm, EditUserForm
from app import db

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

@main.route('/create_role', methods=["GET", "POST"])
def create_role():
    roles = Role.query.all()
    form = RoleForm()
    if form.validate_on_submit():
        q = Role.query.filter_by(name=form.role_name.data).first()
        if q:
            flash("Papel já cadastrado", category='error')
        else:
            role = Role(name=form.role_name.data)
            db.session.add(role)
            db.session.commit()
            return redirect(url_for('.create_role'))
    return render_template('create_role.html', form=form, roles=roles)

@main.route('/remove_role/<role>')
def remove_role(role):
    q = Role.query.filter_by(name=role).first()
    db.session.delete(q)
    db.session.commit()
    flash('Removido com sucesso!')
    return redirect(url_for('.create_role'))

@main.route('/edit_user/<user_id>')
def edit_user(user_id):
    form = EditUserForm(user_id)
    return render_template('edit_user.html', form=form, user_id=user_id)

@main.route('/users')
def users():
    list_users = User.query.all()
    if not list_users:
        flash('Não existem usuários cadastrados!')
    return render_template('list_users.html', users=list_users)
