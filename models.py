from app import db



class spend(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    #name of credit card
    name= db.Column(db.String,index=True)
    #auto spend 
    auto= db.Column(db.Integer,index=True)
    #travel spend
    travel= db.Column(db.Integer,index=True)
    #online spend
    online=  db.Column(db.Integer,index=True
    #points or pecent cashback
    percent= db.Column(db.Integer,index=True)

    def __repr__(self):
        return f'<spend:{self.name}>'
    