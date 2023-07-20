from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import email_validator, data_required,length


class RegistrationForm(Form):
    name = StringField('name', [validators.Length(min=4, max=25)])
    surname = StringField('surname', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])