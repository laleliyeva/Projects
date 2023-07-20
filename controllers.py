from app import app
from models import *
from flask import render_template


@app.route('/credits/')
def credits():
    return render_template('cards.html')
   
@app.route('/credit_detail/')
def credit_detail():
    return render_template('kreditkalkulyatoru.html')

@app.route('/xeber/')
def xeber():
    return render_template('xeberler.html')

@app.route('/xeber_detail/')
def xeber_detail():
    return render_template('xeber1.html')

    
    
