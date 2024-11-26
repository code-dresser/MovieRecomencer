from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

login_manager = LoginManager()
bcrypt = Bcrypt()
db=SQLAlchemy()