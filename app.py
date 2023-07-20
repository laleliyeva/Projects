from flask import Flask

app= Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/bank_db"
app.config['SECRET_KEY']='project'
SQLALCHEMY_TRACK_MODIFICATIONS=True

from extensions import *
from controllers import *
from models import *

if __name__ == '__main__':
    db.init_app(db)
    db.init_app(migrate)
    app.run(port=3306, debug=True)