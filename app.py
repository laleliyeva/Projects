from flask import Flask

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:0001@127.0.0.1:3306/movie_db"
app.config['SECRET_KEY']='project'
SQLALCHEMY_TRACK_MODIFICATIONS=True

from extensions import *
from controllers import *
from models import *

if __name__=='__main__':
    app.run(port=3306,debug=True)
    db.init_app(migrate)
    db.init_app(app)