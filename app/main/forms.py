from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

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

class RoleForm(FlaskForm):
    role_name = StringField('Role', validators=[ DataRequired() ])
    submit = SubmitField('OK')
