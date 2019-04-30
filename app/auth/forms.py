from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('User', validators = [ DataRequired(), Length(min=4, max=50) ])
    password = PasswordField('Password', validators = [ DataRequired(), Length(min=5, max=30) ])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Usuário', validators=[
        DataRequired(),
        Length(min=1, max=64)
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(),
    ])
    password2 = PasswordField('Confirmar senha', validators=[
        DataRequired(),
        EqualTo(password, message='Senhas não conferem')
    ])
    register = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Usuário já registrado")