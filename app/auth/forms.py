from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from ..models import User, Role

class LoginForm(FlaskForm):
    username = StringField('User', validators = [ DataRequired(), Length(1, 64) ])
    password = PasswordField('Password', validators = [ DataRequired() ])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Usuário', validators=[
        DataRequired(),
        Length(1, 64)
    ])
    password = PasswordField('Senha', validators=[
        DataRequired()
    ])
    password2 = PasswordField('Confirmar senha', validators=[
        DataRequired(),
        EqualTo('password', message='Senhas não conferem')
    ])
    register = SubmitField('Cadastrar')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Usuário já registrado")