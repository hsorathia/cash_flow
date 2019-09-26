from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

myFlaskObj = Flask (__name__)

@myFlaskObj.route('/')
def cashFlow():
    username = 'Peasants'
    return render_template('index.html', indexUser = username)

myFlaskObj.run()

@app.route('/register', methods = ["Get", "Post"])
def register():
    try:
        c, conn = connection()
        return ("okay")
    except Exception as e:
        return (str(e))