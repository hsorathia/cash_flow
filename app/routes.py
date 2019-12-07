from flask import render_template, flash, redirect, url_for, request
# from app import app
from flask import current_app as app
from . import db
from .forms import LoginForm, RegistrationForm, InputForm, HomeForm, AdminForm, DeleteCard
from .models import User, UserCards, OurCards
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
# import ast
import os


image_folder = os.path.join('static', 'image')
app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
@app.route('/home')
def home():
    """Home Page
    
    :return: Displays the home page of the website
    """
    
    if current_user.is_authenticated:
        flash(current_user.username)
    filename_logo1 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo1.jpg')
    filename_logo2 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo2.png')
    filename_logo3 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo3.png')
    form = HomeForm()
    if form.validate_on_submit():
        # direct users who interact with this page's buttons to the input page 
        # or login page
        if current_user.is_authenticated:
            return redirect(url_for('input_page'))
        else:
            return redirect(url_for('login'))
    return render_template('home.html', form=form, logo1=filename_logo1, logo2=filename_logo2, logo3=filename_logo3)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page
    
    :return: Page for logging in users 
    """
    if current_user.is_authenticated:
        return redirect(url_for('input_page'))

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
    """Register page
    
    :return: Page for registering users new to the website
    """
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
    """Logout functionality
    
    :return: Logs users out of their accounts
    """
    logout_user()
    return redirect(url_for('home'))


@app.route('/input_page', methods=['GET', 'POST'])
def input_page():
    """Input page
    
    :return: Page for allowing users to register 
    """
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = InputForm()
    # flash(form.errors) lets you know if something in the form failed.
    if form.validate_on_submit():
        # flash('didnt work man')
        card = UserCards(userID=current_user.id, cardName=form.creditCardName.data, onlineEstimate=form.onlineEstimate.data, cbOnlinePercentage=form.cOnlinePercentage.data, travelEstimate=form.travelEstimate.data, cbTravelPercentage=form.cTravelPercentage.data, autoEstimate=form.autoEstimate.data, cbAutoPercentage=form.cAutoPercentage.data)
        db.create_all()
        db.session.add(card)
        db.session.commit()
        flash('Congratulations! You have successfully inputted data')
        return redirect(url_for('output'))
    # else:
    #     flash('didnt work man2')
    return render_template('input.html',  form=form)


# all the credit cards, "output" is misleading
@app.route('/output')
def output():
    """Output/Profile page
    
    :return: Page for displaying all cards owned by a user
    """
    # form = completeForm()
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    usercards = current_user.usercards.all()

    return render_template('output.html', usercards=usercards)

@app.route('/output/delete/<int:id>', methods=['POST'])
def delete(id):
    """Delete Functionality
    
    :return: Route for deleting a specific card from a user
    """
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    card = UserCards.query.filter_by(id=id).all()
    db.create_all()    
    for c in card:    
        db.session.delete(c)
        db.session.commit()
    return redirect(url_for('output'))



@app.route('/comparison')
def comparison():
    """Comparison page
    
    :return: Page that shows the better of two cards and values that depict why that card was better
    """
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    usercards = current_user.usercards.all()
    if usercards is None:
        return redirect(url_for('input'))
    appcards = OurCards.query.all()
    finalCards = {}
    # go through cards in our data base's and calculate values to find the better
    # between two cards
    for card in usercards:
        # bestCard = {}
        finalCards[card] = {}
        for ourcard in appcards:
            normSpend = card.onlineEstimate*card.cbOnlinePercentage + card.travelEstimate*card.cbTravelPercentage + card.autoEstimate*card.cbAutoPercentage
            ourSpend = card.onlineEstimate*ourcard.percentOnline + card.travelEstimate*ourcard.percentTravel + card.autoEstimate*ourcard.percentAuto
            if normSpend >= ourSpend:
                apstr = card.cardName + " cb: " + str(normSpend) + " ocb: " + str(ourSpend)
            else:
                apstr = ourcard.name + " cb : " + str(normSpend) + " ocb: " + str(ourSpend)
            finalCards[card][ourcard] = apstr
        
    return render_template('comparison.html', finalCards=finalCards)

@app.route('/admin', methods=['GET','POST'])
def admin():
    """Admin page
    
    :return: Page for allowing admin users to edit the current database of credit cards
    """
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    # if not admin:
    #     return redirect(url_for('output'))
    
    # redirects user if they're not admins of the website
    if current_user.username == 'bibah':
        form = AdminForm()
        if form.validate_on_submit():
            # flash('didnt work man')
            card = OurCards(name=form.name.data,  percentOnline=form.percentOnline.data, percentTravel=form.percentTravel.data, percentAuto=form.percentAuto.data)
            db.create_all()
            db.session.add(card)
            db.session.commit()
            return redirect(url_for('admin'))
    else:
        flash("did not work")
        return redirect(url_for('home'))
    return render_template('admin.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/register', methods=["Get", "Post"])
# def register():
#     try:
#         c, conn = connection()
#         return ("okay")
#     except Exception as e:
#         return (str(e))
