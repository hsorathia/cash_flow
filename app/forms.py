from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from app.models import User
from wtforms import Form, BooleanField, StringField, PasswordField, validators

import gc



class signUp (FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm = PasswordField('Repeat Password',
                                    validators=[DataRequired(), EqualTo('password')])
    accept_tos = BooleanField(
        'I accept the Terms of Service and Privacy Notice (updated)',
        [validators.Required()])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


# Resource Referenced: https://pythonprogramming.net/flask-user-registration-form-tutorial/

# from config import Config

class loginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')