from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
from flask_cors import cross_origin, CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/anac_db'
CORS(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


class Application(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.Text)
    regDate = db.Column(db.DateTime)

    def __init__(self, data,regDate=None):

        self.data = data
        if regDate is None:
            self.regDate = datetime.utcnow()


class Admin_user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    username=db.Column(db.String(50),unique=True)
    email=db.Column(db.String(50))
    password=db.Column(db.String(200))
    regDate=db.Column(db.DateTime)

    def __init__(self, first_name,last_name,username,email,password,regDate=None):

        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.password=password
        if regDate is None:
            self.regDate=datetime.utcnow()
