from extensions import *
from flask_login import  UserMixin, login_user, logout_user, login_required, current_user,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from app import *
from flask_admin.contrib.sqla import ModelView

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(40),nullable=False)
    last_name=db.Column(db.String(40),nullable=False)
    username=db.Column(db.String(40),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    is_active=db.Column(db.Boolean,nullable=False)
    is_superuser=db.Column(db.Boolean,nullable=False)

    def __init__(self,first_name,last_name,username,email,password,is_active=True,is_superuser=True):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.password=generate_password_hash(password)
        self.is_active=is_active
        self.is_superuser=is_superuser

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self,new_password):
        self.new_password=generate_password_hash(new_password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

class Stories(db.Model):
    __tablename__='Stories'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255) , nullable = False)
    img = db.Column(db.String(255) , nullable  = False)
    text = db.Column(db.String(255), nullable=False)
    text_bg = db.Column(db.String(50) , nullable=False)

    def __repr__(self):
        return self.title ,self.text
    
    def __init__(self,title,img,text,text_bg):
        self.title = title
        self.img = img
        self.text = text
        self.text_bg = text_bg

    def save(self):
        db.session.add(self)
        db.session.commit()   


class Cards(db.Model):
    __tablename__ = 'Cards'
    id = db.Column(db.Integer , primary_key = True)
    card_img = db.Column(db.Text)
    card_name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    duration = db.Column(db.String(50) , default= 'Müddet')
    duration_v = db.Column(db.String(50))
    currency = db.Column(db.String(50) , default='Valyuta' )
    currency_v = db.Column(db.String(50))
    cashback = db.Column(db.String(50) , )
    cashback_v = db.Column(db.String(255) , nullable=False)


    def __repr__(self):
        return self.card_name
    
    def __init__(self, card_img,card_name,description,duration,duration_v,currency,currency_v,cashback,cashback_v):
        self.card_img = card_img
        self.card_name = card_name
        self.description = description
        self.duration = duration
        self.duration_v = duration_v
        self.currency = currency
        self.currency_v = currency_v
        self.cashback = cashback
        self.cashback_v = cashback_v

    def save(self):
        db.session.add(self)
        db.session.commit() 


class CardOrder(db.Model):
    __tablename__ = 'CardOrder'
    id = db.Column(db.Integer , primary_key = True)
    card_type = db.Column(db.String(30) , nullable = False)
    currency = db.Column(db.String(20) , nullable = False)
    name = db.Column(db.String(30) , nullable = False)
    surname = db.Column(db.String(50) , nullable = False)
    mobile_number = db.Column(db.String(20) , nullable = False)
    fin_code = db.Column(db.String(7) , nullable = False)
    odenis_usulu = db.Column(db.String(255) , nullable = False)
    secret_word = db.Column(db.String(30) , nullable = False)
    elde_etme_usulu = db.Column(db.String(255) , nullable = False)
    odenis_usulu2 = db.Column(db.String(255) , nullable = False)
    card_id = db.Column(db.Integer , db.ForeignKey('Cards.id'))

    def __repr__(self):
        return self.card_type
    
    def __init__(self, card_type , currency , name , surname ,mobile_number , fin_code , odenis_usulu , secret_word , elde_etme_usulu , odenis_usulu2 , card_id):
        self.card_type = card_type
        self.currency = currency
        self.name = name
        self.surname = surname
        self.mobile_number = mobile_number
        self.fin_code = fin_code
        self.odenis_usulu = odenis_usulu
        self.secret_word = secret_word
        self.elde_etme_usulu  = elde_etme_usulu
        self.odenis_usulu2 = odenis_usulu2
        self.card_id = card_id

    def save(self):
        db.session.add(self)
        db.session.commit()



class CardDetails(db.Model):
    __tablename__ = 'CardDetails'
    id = db.Column(db.Integer , primary_key = True)
    phone_img = db.Column(db.Text)
    icon = db.Column(db.Text)
    title = db.Column(db.String(255) ,  nullable = False)

    def __repr__(self):
        return self.title
    
    def __init__(self,phone_img , icon , title):
        self.phone_img = phone_img
        self.icon = icon
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

admin.add_view(ModelView(Stories , db.session))
admin.add_view(ModelView(Cards , db.session))
admin.add_view(ModelView(CardOrder , db.session))
admin.add_view(ModelView(CardDetails , db.session))









    



