from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
basedir = os.path.abspath(os.path.dirname(__name__))
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

dbdummy=SQLAlchemy()
def create_app(test_config=None):
    appDummy = Flask(__name__, instance_relative_config=True)
    appDummy.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        appDummy.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        appDummy.config.update(test_config)
    
    try:
        os.makedirs(appDummy.instance_path)
    except OSError:
        pass
    dbdummy.init_app(appDummy)

    return app

from app import routes, models