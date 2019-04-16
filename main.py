from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os

BASE_DIR = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'uma chave qualquer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' %(self.name)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %(self.username)

"""
Tipos de dados

BooleanFieldDateField
DateTimeField
DecimalField
FileField
HiddenField
MultipleField
FieldList
FloatField
IntegerField
PasswordField
RadioField
SelectField
SelectMultipleField
SubmitField
StringField
TextAreaField
"""

"""
Validators

DataRequired()
Email()
EqualTo()
FileRequired()
"""


class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[ DataRequired() ])
    submit = SubmitField('Enviar')


@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        nome_anterior = session.get('name')
        if nome_anterior is not None and nome_anterior != form.name.data:
            flash('Parece que você alterou o nome!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/navegador')
def navegador():
    user_agent = request.headers.get('User-Agent')
    return "<p>Seu navegador: %s.</p>" %(user_agent)


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404

