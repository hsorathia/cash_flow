from app import app
from app import db

if __name__ == '__cashflow__':
    db.create_all()
    app.run(debug = True)