from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired
from app.models import User
import gc

class HomeForm(FlaskForm):
    submit = SubmitField('Get Started')



class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password:', validators=[
                              DataRequired(), EqualTo('password')])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class InputForm(FlaskForm):
    creditCardName = StringField('Enter your current credit card:', validators=[InputRequired()])
    onlineEstimate = DecimalField('Online Purchase Estimate: ', validators=[InputRequired()])
    travelEstimate = DecimalField('Travel Purchase Estimate: ', validators=[InputRequired()])
    autoEstimate = DecimalField('Auto Purchase Estimate: ', validators=[InputRequired()])
    cOnlinePercentage = DecimalField('Cash Back Percentage: ', validators=[InputRequired()])
    cTravelPercentage = DecimalField('Cash Back Percentage: ', validators=[InputRequired()])
    cAutoPercentage = DecimalField('Cash Back Percentage: ', validators=[InputRequired()])
    # creditCardName = StringField('Enter your current credit card:')
    # onlineEstimate = IntegerField('Online Purchase Estimate: ')
    # travelEstimate = IntegerField('Travel Purchase Estimate: ')
    # autoEstimate = IntegerField('Auto Purchase Estimate: ')
    # cOnlinePercentage = IntegerField('Cash Back Percentage: ')
    # cTravelPercentage = IntegerField('Cash Back Percentage: ')
    # cAutoPercentage = IntegerField('Cash Back Percentage: ')
    submit = SubmitField('Submit')


