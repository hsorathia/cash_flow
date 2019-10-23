from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from signup import SignUp


app = Flask(__name__)


@app.route('/')
def cashFlow():
    username = 'Peasants'
    form = SignUp()
    return render_template('signup.html', indexUser=username, form=form)


app.run(debug=True)


# @app.route('/register', methods=["Get", "Post"])
# def register():
#     try:
#         c, conn = connection()
#         return ("okay")
#     except Exception as e:
#         return (str(e))
