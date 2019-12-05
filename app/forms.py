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
    cOnlinePercentage = DecimalField('Online Cash Back Percentage: ', validators=[InputRequired()])
    cTravelPercentage = DecimalField('Travel Cash Back Percentage: ', validators=[InputRequired()])
    cAutoPercentage = DecimalField('Automotive Cash Back Percentage: ', validators=[InputRequired()])
    submit = SubmitField('Submit')


class AdminForm(FlaskForm):
    name = StringField('Enter your current credit card:', validators=[InputRequired()])
    percentOnline = DecimalField('Online Cash Back Percentage: ', validators=[InputRequired()])
    percentTravel = DecimalField('Travel Cash Back Percentage: ', validators=[InputRequired()])
    percentAuto = DecimalField('Automotive Cash Back Percentage: ', validators=[InputRequired()])
    submit = SubmitField('Submit')

class DeleteCard(FlaskForm):
    # creditCardName = StringField('Card Name:', validators=[InputRequired()])
    submit = SubmitField('Delete Card')