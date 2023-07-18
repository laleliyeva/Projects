from app import app
from flask import render_template,  request,redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import *
from models import *
from flask_login import login_user, login_required
from werkzeug.security import check_password_hash