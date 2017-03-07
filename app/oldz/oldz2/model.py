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


#classes
class Application(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    aeronefs = db.Column(db.String(200))
    personels = db.Column(db.String(200))
    raison_social = db.Column(db.String(100))
    addresse_sociale = db.Column(db.String(100))
    addresse_telephone = db.Column(db.String(20))
    addresse_electronique = db.Column(db.String(50))
    autre_appelation = db.Column(db.String(200))
    address_admin = db.Column(db.String(100))
    etablissement_sec = db.Column(db.String(100))
    type_exploitation = db.Column(db.String(100))
    date_commencemment = db.Column(db.DateTime)
    regions_geographiques = db.Column(db.String(100))
    formations_proposees = db.Column(db.String(100))
    type_organisation = db.Column(db.String(100))
    nom_applicant = db.Column(db.String(100))
    prenom_applicant = db.Column(db.String(100))
    titre_applicant = db.Column(db.String(100))
    regDate = db.Column(db.DateTime)
    Personal = db.relationship('Personal', backref='application', lazy='dynamic')
    Aeronof = db.relationship('Aeronef', backref='application', lazy='dynamic')


    def __init__(self, raison_social, addresse_sociale, addresse_telephone, addresse_electronique, autre_appelation, address_admin,etablissement_sec, type_exploitation, date_commencemment, regions_geographiques, formations_proposees,type_organisation, nom_applicant, prenom_applicant, titre_applicant, regDate=None):

        self.raison_social = raison_social
        self.addresse_sociale = addresse_sociale
        self.addresse_telephone = addresse_telephone
        self.addresse_electronique = addresse_electronique
        self.autre_appelation = autre_appelation
        self.address_admin = address_admin
        self.etablissement_sec = etablissement_sec
        self.type_exploitation = type_exploitation
        self.date_commencemment = date_commencemment
        self.regions_geographiques = regions_geographiques
        self.formations_proposees = formations_proposees
        self.type_organisation = type_organisation
        self.nom_applicant = nom_applicant
        self.prenom_applicant = prenom_applicant
        self.titre_applicant = titre_applicant
        if regDate is None:
            self.regDate=datetime.utcnow()


class Personnel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    applic_id=db.Column(db.Integer, db.ForeignKey('application.id'))
    names = db.Column(db.String(100))
    title = db.Column(db.String(100))
    telephone = db.Column(db.String(20))
    telecopieur = db.Column(db.String(20))
    email = db.Column(db.String(50))

    def __init__(self, applic_id, names, title, telephone, telecopieur, email):

        self.applic_id = applic_id
        self.names = names
        self.title = title
        self.telephone = telephone
        self.telecopieur = telecopieur
        self.email = email


class Aeronefs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applic_id = db.Column(db.Integer, db.ForeignKey('application.id'))
    type_aeronef = db.Column(db.String(50))
    marque = db.Column(db.String(50))
    model = db.Column(db.String(50))
    nationalite = db.Column(db.String(50))
    immatriculaton = db.Column(db.String(50))
    passagers = db.Column(db.Integer)
    capacite = db.Column(db.Integer)
    loue = db.Column(db.Boolean)
    link = db.Column(db.String(100))

    def __init__(self, applic_id, type_aeronef, marque, model, nationalite, immatriculaton, passagers, capacite, loue, link):

        self.applic_id = applic_id
        self.type_aeronef = type_aeronef
        self.marque = marque
        self.model = model
        self.nationalite = nationalite
        self.immatriculaton = immatriculaton
        self.passagers = passagers
        self.capacite = capacite
        self.loue = loue
        self.link = link



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
