from . import db
from . import login
from flask_login import UserMixin


from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    usercards = db.relationship('UserCards', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class UserCards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    # name of credit card
    cardName = db.Column(db.String, index=True)
    # online spend
    onlineEstimate = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None), index=True)
    # points or pecent cashback online
    cbOnlinePercentage = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None), index=True)
    # travel spend
    travelEstimate = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None), index=True)
    # points or pecent cashback travel
    cbTravelPercentage = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None), index=True)
    # auto spend
    autoEstimate = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None), index=True)
    # points or pecent cashback auto
    cbAutoPercentage = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None), index=True)

    def __repr__(self):
        return f'Card: {self.cardName}'


class OurCards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)

    percentOnline = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None), index=True)
    percentTravel = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None), index=True)
    percentAuto = db.Column(db.Numeric(precision=2, asdecimal=False, decimal_return_scale=None), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
