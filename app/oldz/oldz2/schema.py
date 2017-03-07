from marshmallow import Schema,fields

class ApplicationSchema(Schema):

    id=fields.Integer(dump_only=True)
    aeronefs = fields.String()
    personels = fields.String()
    raison_social = fields.String()
    addresse_sociale = fields.String()
    addresse_telephone = fields.String()
    addresse_electronique = fields.String()
    autre_appelation = fields.String()
    address_admin = fields.String()
    etablissement_sec = fields.String()
    type_exploitation = fields.String()
    date_commencemment = fields.Date()
    regions_geographiques = fields.String()
    formations_proposees = fields.String()
    type_organisation = fields.String()
    nom_applicant = fields.String()
    prenom_applicant = fields.String()
    titre_applicant = fields.String()
    regDate = fields.Date()

appl_schema = ApplicationSchema()
appls_schema = ApplicationSchema(many = True)



class AeronefSchema(Schema):

    id = fields.Integer(dump_only=True)
    applic_id = fields.Integer()
    type_aeronef = fields.String()
    marque = fields.String()
    model = fields.String()
    nationalite = fields.String()
    immatriculaton = fields.String()
    passagers = fields.Integer()
    capacite = fields.Integer()
    loue = fields.Boolean()
    link = fields.String()

aero_schema = AeronefSchema()
aeros_schema = AeronefSchema(many = True)


class PersonelSchema(Schema):

    id = fields.Integer(dump_only=True)
    applic_id=fields.Integer()
    names = fields.String()
    title = fields.String()
    telephone = fields.String()
    telecopieur = fields.String()
    email = fields.String()

perso_schema = PersonalSchema()
persos_schema = PersonalSchema(many = True)



class Admin_userSchema(Schema):
    id=fields.Integer(dump_only=True)
    first_name=fields.String()
    last_name=fields.String()
    username=fields.String()
    email=fields.String()
    password=fields.String()
    regDate=fields.Date()

useradmin_schema=Admin_userSchema()
useradmins_schema=Admin_userSchema(many=True)
