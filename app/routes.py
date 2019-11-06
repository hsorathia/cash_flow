from flask import Flask, render_template, flash, redirect, url_for
from app import app
from app.forms import loginForm, signUp
from app.models import User
from flask_login import current_user, login_user
import os
image_folder = os.path.join('static', 'image')
app.config['UPLOAD_FOLDER'] = image_folder
@app.route('/')
@app.route('/home')
def home():
    filename_logo1 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo1.jpg')
    filename_logo2 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo2.png')
    filename_logo3 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo3.png')
    return render_template('home.html', logo1=filename_logo1, logo2=filename_logo2, logo3=filename_logo3)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        userName = User.query.filter_by(username = form.username.data).first()
       
        if userName is None or not userName.check_password(form.password.data):
            flash('invalid username or password')
        else:
            flash('you have succesfully logged in')
            login_user(user, remember=form.form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(url_for(next_page))

        # flash('Hello you logged in')
        # flash('Login requested for user {}, rememberMe={}'.format(
        #     form.username.data, form.rememberMe.data))
        
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = signUp()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/output')
def output():
    # form = completeForm()
    valid = False

    return render_template('output.html', valid=valid)


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/register', methods=["Get", "Post"])
# def register():
#     try:
#         c, conn = connection()
#         return ("okay")
#     except Exception as e:
#         return (str(e))