from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

from app import app
from flask_login import LoginManager



db = SQLAlchemy(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
admin = Admin(app , name = 'YeloBank' , template_mode = 'bootstrap4')
