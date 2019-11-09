from flask import render_template, flash, redirect, url_for, request
from app import app
from app import db
from app.forms import LoginForm, RegistrationForm, InputForm, HomeForm
from app.models import User, UserCards
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import os


image_folder = os.path.join('static', 'image')
app.config['UPLOAD_FOLDER'] = image_folder
@app.route('/')
@app.route('/home')
def home():

    filename_logo1 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo1.jpg')
    filename_logo2 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo2.png')
    filename_logo3 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo3.png')
    form = HomeForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return redirect(url_for('input_page'))
        else:
            return redirect(url_for('login'))
    return render_template('home.html', form=form, logo1=filename_logo1, logo2=filename_logo2, logo3=filename_logo3)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.rememberMe.data)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('input_page')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/input_page', methods=['GET', 'POST'])
def input_page():
    form = InputForm()
    flash(form.errors)
    if form.validate_on_submit():
        flash('didnt work man')
        card = UserCards(author=current_user, cardName=form.creditCardName.data, onlineEstimate=form.onlineEstimate.data, cbOnlinePercentage=form.cOnlinePercentage.data, travelEstimate=form.travelEstimate.data, cbTravelPercentage=form.cTravelPercentage.data, autoEstimate=form.autoEstimate.data, cbAutoPercentage=form.cAutoPercentage.data)
        db.create_all()
        db.session.add(card)
        db.session.commit()
        flash('Congratulations! You have successfully inputted data')
        return redirect(url_for('output'))
    else:
        flash('didnt work man2')
    return render_template('input.html',  form=form)


@app.route('/output')
def output():
    # form = completeForm()
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    usercards = current_user.usercards.all()
    return render_template('output.html', usercards=usercards)


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/register', methods=["Get", "Post"])
# def register():
#     try:
#         c, conn = connection()
#         return ("okay")
#     except Exception as e:
#         return (str(e))
