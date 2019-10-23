from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, StringField, PasswordField, validators
#from passlib.hash import sha256_crypt
#from MySQLdb import escape_string as thwart
import gc

# Forms a class with the username, pw, and email


class signUp (Form):
    username = StringField('Username',
                           # validators = parameters set for specification
                           [validators.Length(min=4, max=32)])
    email = StringField('Email Address',
                        [validators.Length(min=4, max=100)])
    password = PasswordField('New Password',
                             [validators.Required(),
                              validators.EqualTo(
                                  'confirm', message='Passwords need to match')
                              ])

    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField(
        'I accept the Terms of Service and Privacy Notice (updated)',
        [validators.Required()])


# Resource Referenced: https://pythonprogramming.net/flask-user-registration-form-tutorial/

# from config import Config


class loginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')
