from flask import Flask


app=Flask(__name__, template_folder='templates' , static_folder='static')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:0001@127.0.0.1:3306/project"
SQLALCHEMY_TRACK_MODIFICATIONS=True
app.config['FLASK_ADMIN_SWATCH']='cerulean'
app.config['SECRET_KEY']='YeloBank'


from extensions import *
from controllers import *
from models import *
from forms import *

if __name__=='__main__':
    app.run(port=3306,debug=True)
    db.init_app(migrate)
    db.init_app(app)