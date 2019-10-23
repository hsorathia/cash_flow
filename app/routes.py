from flask import Flask, render_template, flash, redirect, url_for

from app import app

from app.forms import loginForm
from app.forms import signUp


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = loginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, rememberMe={}'.format(
            form.username.data, form.rememberMe.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/output')
def output():
    # form = completeForm()
    valid = False

    return render_template('output.html', valid=valid)


app.run(debug=True)


# @app.route('/register', methods=["Get", "Post"])
# def register():
#     try:
#         c, conn = connection()
#         return ("okay")
#     except Exception as e:
#         return (str(e))
