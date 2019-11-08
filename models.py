from app import db
from app import login
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class spend(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    #name of credit card
    name= db.Column(db.String,index=True)
    #online spend
    online=  db.Column(db.Integer,index=True)
    #points or pecent cashback online
    percentO= db.Column(db.Integer,index=True)
    #travel spend
    travel= db.Column(db.Integer,index=True)
    #points or pecent cashback travel
    percentT= db.Column(db.Integer,index=True)
    #auto spend 
    auto= db.Column(db.Integer,index=True)
    #points or pecent cashback auto
    percentA= db.Column(db.Integer,index=True)
    
    def __repr__(self):
        return f'<spend:{self.name}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
