from flask import render_template, request, session, url_for, redirect, flash
from flask_login import login_required, current_user

from app.models import Role, User, Permission, Post
from . import main
from .forms import NameForm, RoleForm, EditUserForm, PostForm
from app import db

@main.route("/", methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.has_permission(Permission.WRITE) and form.validate_on_submit():
        post = Post(
            body=form.body.data,
            author=current_user._get_current_object()
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template('index.html', form=form, posts=posts)

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

@main.route('/users')
def users():
    list_users = User.query.all()
    if not list_users:
        flash('Não existem usuários cadastrados!')
    return render_template('list_users.html', users=list_users)

@main.route('/edit_user/<username>', methods=["GET", "POST"])
def edit_user(username):
    u = User.query.filter_by(username=username).first()
    form = EditUserForm(user=u)
    if form.validate_on_submit():
        selected_item = [tuple[1] for tuple in form.role_choices if tuple[0] == form.role.data][0]
        r = Role.query.filter_by(name=selected_item).first()
        u.role_id = r.id
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('.users'))
    return render_template('edit_user.html', form=form)

