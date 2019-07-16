import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# import flask_sqlalchemy
# import flask_bcrypt
# import flask_login

app = Flask(__name__)

# Disables track modification warning 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.secret_key = os.environ.get('MY_DBTXT_GAME_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from dragonb_game import routes
