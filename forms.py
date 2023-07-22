from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField,PasswordField , SelectField , SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])

class OrderForm(FlaskForm):  
    card_type = SelectField('Card Type', choices = [('', 'Card Type'), ('VISA', 'VISA'), ('Mastercard', 'Mastercard')], validators=[DataRequired()])
    currency = SelectField('Currency', choices = [('', 'Currency'), ('AZN', 'AZN'), ('USD', 'USD'), ('EUR', 'EUR')], validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    mobile_number = IntegerField('Mobile Number', validators=[DataRequired()], render_kw={'placeholder': 'mobile'})
    pin = StringField('PIN', validators=[DataRequired(), Length(min=7, max=7)], render_kw={'placeholder': 'pin'})
    payment_methods = SelectField('Payment Methods', choices = [('', 'Payment Method'), ('price', 'With the payment of the card price'), ('deposit', 'With initial deposit')], validators=[DataRequired()])
    secret_word = StringField('Secret Word', validators=[DataRequired(), Length(min=1, max=7)])
    method_ac = SelectField('Method of acquisition', choices = [('', 'Method of acquisition'), ('Delivery', 'Delivery - Free'), ('branch', 'In bank branch')], validators=[DataRequired()])
    payment_type = SelectField('Payment type', choices = [('', 'Payment type'), ('Via', 'Via terminal')], validators=[DataRequired()])