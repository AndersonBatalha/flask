from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models import Role, User

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

class PostForm(FlaskForm):
    body = TextAreaField('O que você está pensando?',
                         validators=[
                             DataRequired()
                         ])
    submit = SubmitField('Enviar')


class RoleForm(FlaskForm):
    role_name = StringField('Role', validators=[ DataRequired() ])
    submit = SubmitField('OK')

class EditUserForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    role = SelectField("Role", coerce=int)
    submit = SubmitField('Enviar')

    def __init__(self, user, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.role_choices = [
            (role.id, role.name) for role in Role.query.order_by(Role.name).all()
        ]
        self.role.choices = self.role_choices
        self.user = user
        self.username.data = self.user.username

class EditProfileAdminForm(FlaskForm):
    username = StringField('Usuário', validators=[
        DataRequired(), Length(1,64)
    ])
    role = SelectField("Função", coerce=int)
    name = StringField("Nome completo", validators=[
        Length(1,64)
    ])
    about_me = TextAreaField("Sobre mim")
    submit = SubmitField("Enviar")

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [
            (role.id, role.name) for role in Role.query.order_by(Role.name).all()
        ]
        self.user = user

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Usuário já existe!')

