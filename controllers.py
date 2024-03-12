from flask import render_template , request , redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import *
from models import *
from flask_login import login_user, login_required
from werkzeug.security import check_password_hash


@app.route('/credits/')
def creditss():
    m1 = kredit.query.all()
    return render_template('creditcard1.html' , m1=m1)
   
@app.route('/credit_detail/')
def credit_detaill():
    m1 = kredit.query.all()
    return render_template('kreditkalkulyatoru.html', m1=m1)

@app.route('/xeber/')
def xeberr():
    x1 = Xeber.query.all()
    return render_template('xeberler.html' , x1=x1)

@app.route('/xeber_detail/<int:xeber_id>/')
def xeber_detaill(xeber_id):
    x1 = Xeber.query.filter_by(id=xeber_id).first()
    return render_template('xeber1.html', x1=x1)

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
    return render_template ('menu.html')


@app.route('/card/<int:card_id>/', methods=['GET', 'POST'])
def detail_page(card_id):
    card_info = Cards.query.get(card_id)
    card_detail = CardDetails.query.filter_by(card_id=card_id).first()
    all_data = request.form
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(data=all_data)
        if form.validate_on_submit():
            order_data = CardOrder(card_type=form.card_type.data,currency=form.currency.data,
                                   name=form.name.data,surname=form.surname.data,mobile_number=form.mobile_number.data,
                                   fin_code=form.pin.data,odenis_usulu=form.payment_methods.data,
                                   secret_word=form.secret_word.data,elde_etme_usulu=form.method_ac.data,
                                   odenis_usulu2=form.payment_type.data, card_id=card_id)

            db.session.add(order_data)
            db.session.commit()

    return render_template('cards_info.html', card_info=card_info, card_detail=card_detail, form=form)

@app.route('/cards/')
def all_cards():
    all_cards_list = Cards.query.all()
    return render_template('cards.html', all_cards_list=all_cards_list)


@app.route('/ordercard/', methods=['GET', 'POST'])
def recmovie():
    form = OrderForm()
    alldata = request.form
    if request.method == "POST":
        form=OrderForm(data=alldata)
        if form.validate_on_submit():
            order_data = OrderForm(
        kart_novu = form.card.data,
        valyuta = form.valyuta.data,
        ad = form.ad.data,
        soyad = form.soyad.data,
        mobil_nomre = form.phone.data,
        fin = form.fin.data,
        odenis_usulu = form.odenis_usulu.data,
        mexfi_soz = form.mexfi_soz.data,
        elde_etme_usulu = form.elde_etme_usulu.data,
        odenis_vasitesi = form.odenis_vasitesi.data)
            
            order_data.save()
    
    return render_template('cards_info.html', form=form)