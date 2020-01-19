import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

'''
Flask(__name__) is a class/prototype imported from the flask framework and is 
used to create an instance of a web application. On this case I am creating an 
instance of a flask web application and saving it to the variable "app". The 
variable __name__ will hold the value "dragonb_game"(which is the name of the 
module/application) and not "__main__" since this script/file is not being run 
directly, but imported into run.py which is the file being run directly.
'''
app = Flask(__name__)

# Disables track modification warning 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Protects against modifying cookies and cross-site request and forgery attacks
app.secret_key = os.environ.get('MY_DBTXT_GAME_KEY')
# Choosing a database server to where we can persist our data
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Facilitates data persisting into data base by means of use object relational mapper
db = SQLAlchemy(app)
# Data security- emcrypting users' password 
bcrypt = Bcrypt(app)
# Manages users' sessions
login_manager = LoginManager(app)
# Manages and validates users' views to certain routes.
login_manager.login_view = 'login'
# Manages messages displays/statics/colors to users
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
mail = Mail(app)

from dragonb_game import routes
