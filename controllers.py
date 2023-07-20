from app import app
from flask import render_template , request , redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import *
from models import *
from flask_login import login_user, login_required
from werkzeug.security import check_password_hash

@app.route('/')
def main_page():
    all_stories = Stories.query.all()
    return render_template('index.html' , stories=all_stories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        all_data = request.form
        form = RegisterForm(data=all_data)
        if form.validate_on_submit():
            new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data, email=form.email.data, password=form.password.data,is_active=True)
            new_user.save()
        else:
            print('Qeydiyyat ugursuz oldu')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        all_data = request.form
        form = LoginForm(data=all_data)
        if form.validate_on_submit():
            new_user = User.query.filter_by(username=form.username.data).first()
            if new_user and check_password_hash(new_user.password, form.password.data):
                login_user(new_user)
                return redirect('/admin')
            else:
                print('Daxil olmaq mümkün olmadı. İstifadəçi adı və ya şifrə yanlışdır.')
    return render_template('login.html', form=form)


@app.route('/menu/')
def menu():
    render_template ('menu.html')

@app.route('/card/<int:card_id>')
def detail_page(card_id):
    card = Cards.query.filter_by(id=card_id).first()
    if card:
        return render_template('cards_info.html' , card=card)

@app.route('/cards/')
def all_cards():
    cards = Cards.query.all()
    return render_template('cards.html', cards=cards)




