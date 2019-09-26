from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField

class loginForm(FlaskForm):
    username = StringField('Username:')
    password = PasswordField('Password:')
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')
    