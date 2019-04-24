from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('User', validators = [ DataRequired(), Length(min=4, max=50) ])
    password = PasswordField('Password', validators = [ DataRequired(), Length(min=5, max=30) ])
    submit = SubmitField('Login')