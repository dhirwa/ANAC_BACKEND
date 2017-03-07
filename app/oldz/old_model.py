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
    id=db.Column(db.Integer,primary_key=True)
    type_demand = db.Column(db.String(50))
    license = db.Column(db.Boolean)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    passport_id_Card=db.Column(db.String(50))
    birthdate=db.Column(db.DateTime)
    birth_place=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    address=db.Column(db.String(50))
    resid_city=db.Column(db.String(50))
    resid_state=db.Column(db.String(50))
    resid_country=db.Column(db.String(50))
    postal_code=db.Column(db.String(50))
    phone = db.Column(db.String(50))
    email=db.Column(db.String(50))
    nationality=db.Column(db.String(50))
    weight=db.Column(db.Integer)
    height=db.Column(db.Integer)
    hair=db.Column(db.String(50))
    eyes=db.Column(db.String(50))
    curr_lic_detention = db.Column(db.Boolean)
    lic_eversusp = db.Column(db.Boolean)
    type_license=db.Column(db.String(50))
    lic_number=db.Column(db.String(50))
    lic_issue_date=db.Column(db.DateTime)
    underst_french=db.Column(db.Boolean)
    underst_english=db.Column(db.Boolean)
    knowledge_test=db.Column(db.Boolean)
    test_applied_for = db.Column(db.String(50))
    test_success = db.Column(db.String(50))
    date_of_test_compl = db.Column(db.String(50))
    skillTest=db.Column(db.Boolean)
    aircraft = db.Column(db.String(50))
    time_in_aircraft =db.Column(db.Integer)
    hours_of_flight=db.Column(db.Integer)
    graduate_ato = db.Column(db.Boolean)
    name_institution = db.Column(db.String(100))
    inst_city=db.Column(db.String(50))
    inst_state=db.Column(db.String(50))
    inst_country=db.Column(db.String(50))
    ato_certiciate_no = db.Column(db.String(50))
    grad_date=db.Column(db.DateTime)
    holder_foreign_lic=db.Column(db.Boolean)
    foreignlic_country=db.Column(db.String(50))
    type_of_foreign_lic=db.Column(db.String(50))
    lic_rating= db.Column(db.String(50))
    military_competence = db.Column(db.Boolean)
    service=db.Column(db.String(100))
    milit_grad_date=db.Column(db.DateTime)
    service_number = db.Column(db.String(50))
    has_flied_10hours =db.Column(db.Boolean)
    last_flight_Check_date=db.Column(db.DateTime)
    final_certifying = db.Column(db.Boolean)
    regDate=db.Column(db.DateTime)

    Recommandation = db.relationship('Recommandation', backref='application', lazy='dynamic')
    SkillTest = db.relationship('SkillTest', backref='application', lazy='dynamic')
    Anac_Report = db.relationship('Anac_Report', backref='application', lazy='dynamic')
    Final_Issuance=db.relationship('Final_Issuance',backref='application',lazy='dynamic')

    def __init__(self ,type_demand,license,first_name,last_name,passport_id_Card,birthdate,birth_place,gender,address,resid_city,resid_state,resid_country,postal_code,phone,email,nationality,weight,height,hair,eyes,curr_lic_detention,lic_eversusp,type_license,lic_number,lic_issue_date,underst_french,underst_english,knowledge_test,test_applied_for,test_success,date_of_test_compl,skillTest,aircraft,time_in_aircraft,hours_of_flight,graduate_ato,name_institution,inst_city,inst_state,inst_country,ato_certiciate_no,grad_date,holder_foreign_lic,foreignlic_country,type_of_foreign_lic,lic_rating,military_competence,service,milit_grad_date,service_number,has_flied_10hours,last_flight_Check_date,final_certifying,regDate=None):

        self.type_demand=type_demand
        self.license=license
        self.first_name=first_name
        self.last_name=last_name
        self.passport_id_Card=passport_id_Card
        self.birthdate= birthdate
        self.birth_place=birth_place
        self.gender=gender
        self.address=address
        self.resid_city=resid_city
        self.resid_state=resid_state
        self.resid_country=resid_country
        self.postal_code=postal_code
        self.phone=phone
        self.email=email
        self.nationality=nationality
        self.weight=weight
        self.height=height
        self.hair=hair
        self.eyes=eyes
        self.curr_lic_detention=curr_lic_detention
        self.lic_eversusp=lic_eversusp
        self.type_license=type_license
        self.lic_number=lic_number
        self.lic_issue_date=lic_issue_date
        self.underst_french=underst_french
        self.underst_english=underst_english
        self.knowledge_test=knowledge_test
        self.test_applied_for=test_applied_for
        self.test_success=test_success
        self.date_of_test_compl=date_of_test_compl
        self.skillTest=skillTest
        self.aircraft=aircraft
        self.time_in_aircraft=time_in_aircraft
        self.hours_of_flight=hours_of_flight
        self.graduate_ato=graduate_ato
        self.name_institution=name_institution
        self.inst_city=inst_city
        self.inst_state=inst_state
        self.inst_country=inst_country
        self.ato_certiciate_no=ato_certiciate_no
        self.grad_date=grad_date
        self.holder_foreign_lic=holder_foreign_lic
        self.foreignlic_country=foreignlic_country
        self.type_of_foreign_lic=type_of_foreign_lic
        self.lic_rating=lic_rating
        self.military_competence=military_competence
        self.service=service
        self.milit_grad_date=milit_grad_date
        self.service_number=service_number
        self.has_flied_10hours=has_flied_10hours
        self.last_flight_Check_date=last_flight_Check_date
        self.final_certifying=final_certifying
        if regDate is None:
            self.regDate=datetime.utcnow()



class Recommandation(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    applic_id=db.Column(db.Integer, db.ForeignKey('application.id'))
    service_number=db.Column(db.String(50))
    personally_instructed=db.Column(db.Boolean)
    date_of_instr=db.Column(db.DateTime)
    name_of_instr=db.Column(db.String(50))
    license_number=db.Column(db.String(50))
    expiration_date=db.Column(db.DateTime)
    approved_training_org=db.Column(db.Boolean)
    course_completed=db.Column(db.String(50))
    endorsed_test=db.Column(db.String(50))
    ato_date = db.Column(db.DateTime)
    ato_name=db.Column(db.String(100))
    ato_certiciate_no=db.Column(db.String(50))
    name_recommender = db.Column(db.String(50))
    title_recommender = db.Column(db.String(50))
    reviewed_theperson_applicant=db.Column(db.Boolean)
    knowledge_test=db.Column(db.Boolean)
    retake_of_passtest=db.Column(db.Boolean)
    retest_after_failure=db.Column(db.Boolean)
    reviewed_and_not_authorize=db.Column(db.Boolean)
    remarks=db.Column(db.String(300))
    name_inspector=db.Column(db.String(50))
    title_inspector=db.Column(db.String(50))
    date_inspect=db.Column(db.DateTime)


    def __init__(self, applic_id,service_number,personally_instructed,date_of_instr,name_of_instr,license_number,expiration_date,approved_training_org,course_completed,endorsed_test,ato_date,ato_name,ato_certiciate_no,name_recommender,title_recommender,reviewed_theperson_applicant,knowledge_test,retake_of_passtest,retest_after_failure,reviewed_and_not_authorize,remarks,name_inspector,title_inspector,date_inspect ):

        self.applic_id=applic_id
        self.service_number=service_number
        self.personally_instructed=personally_instructed
        self.date_of_instr=date_of_instr
        self.name_of_instr=name_of_instr
        self.license_number=license_number
        self.expiration_date=expiration_date
        self.approved_training_org=approved_training_org
        self.course_completed=course_completed
        self.endorsed_test=endorsed_test
        self.ato_date=ato_date
        self.ato_name=ato_name
        self.ato_certiciate_no=ato_certiciate_no
        self.name_recommender=name_recommender
        self.title_recommender=title_recommender
        self.reviewed_theperson_applicant=reviewed_theperson_applicant
        self.knowledge_test=knowledge_test
        self.retake_of_passtest=retake_of_passtest
        self.retest_after_failure=retest_after_failure
        self.reviewed_and_not_authorize=reviewed_and_not_authorize
        self.remarks=remarks
        self.name=name
        self.name_inspector=name_inspector
        self.title_inspector=title_inspector
        self.date_inspect=date_inspect


class SkillTest(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    applic_id=db.Column(db.Integer, db.ForeignKey('application.id'))
    applicant_meets_reqs=db.Column(db.Boolean)
    applicant_and_results=db.Column(db.Boolean)
    approved=db.Column(db.Boolean)
    disapproved_notice=db.Column(db.Boolean)
    applicant_meets_linguistics=db.Column(db.Boolean)
    ling_french=db.Column(db.Boolean)
    ling_english=db.Column(db.Boolean)
    test_city=db.Column(db.String(50))
    test_state=db.Column(db.String(50))
    test_country=db.Column(db.String(50))
    duration_of_test=db.Column(db.Integer)
    examiner_number=db.Column(db.String(50))
    licensefor_which_tested=db.Column(db.String(50))
    date__test=db.Column(db.DateTime)
    name_examiner=db.Column(db.String(50))

    def __init__(self ,applic_id,applicant_meets_reqs,applicant_and_results,approved,disapproved_notice,applicant_meets_linguistics,ling_french,ling_english,test_city,test_state,test_country,duration_of_test,examiner_number,licensefor_which_tested,date__test,name_examiner):

        self.applic_id=applic_id
        self.applicant_meets_reqs=applicant_meets_reqs
        self.applicant_and_results=applicant_and_results
        self.approved=approved
        self.disapproved_notice=disapproved_notice
        self.applicant_meets_linguistics=applicant_meets_linguistics
        self.ling_french=ling_french
        self.ling_english=ling_english
        self.test_city=test_city
        self.test_state=test_state
        self.test_country=test_country
        self.duration_of_test=duration_of_test
        self.examiner_number=examiner_number
        self.licensefor_which_tested=licensefor_which_tested
        self.date__test=date__test
        self.name_examiner=name_examiner

class Anac_Report(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    applic_id=db.Column(db.Integer, db.ForeignKey('application.id'))
    accepted=db.Column(db.Boolean)
    rejected=db.Column(db.Boolean)
    renewal_license=db.Column(db.Boolean)
    reissue_license=db.Column(db.Boolean)
    issue_certificate=db.Column(db.Boolean)
    other=db.Column(db.Boolean)
    suspended_license=db.Column(db.Boolean)
    knowledge_test_report=db.Column(db.Boolean)
    skillTest_Report=db.Column(db.Boolean)
    notice_denial=db.Column(db.Boolean)
    grad_certificate=db.Column(db.Boolean)
    copy_identification=db.Column(db.Boolean)
    verif_auth=db.Column(db.Boolean)
    government_identification=db.Column(db.String(50))
    identification_number=db.Column(db.String(50))
    expiration_date=db.Column(db.DateTime)
    certificate_maybe_issued = db.Column(db.Boolean)
    applicant_missing_documents = db.Column(db.Boolean)
    name_inspector=db.Column(db.String(50))
    title_inspector=db.Column(db.String(50))
    date = db.Column(db.DateTime)

    def __init__(self, applic_id,accepted,rejected,renewal_license,reissue_license,issue_certificate,other,suspended_license,knowledge_test_report,skillTest_Report,notice_denial,grad_certificate,copy_identification,verif_auth,government_identification,identification_number,expiration_date,certificate_maybe_issued,applicant_missing_documents,name_inspector,title_inspector,date):

        self.applic_id= applic_id
        self.accepted= accepted
        self.rejected= rejected
        self.renewal_license=renewal_license
        self.reissue_license=reissue_license
        self.issue_certificate=issue_certificate
        self.other=other
        self.suspended_license=suspended_license
        self.knowledge_test_report=knowledge_test_report
        self.skillTest_Report=skillTest_Report
        self.notice_denial=notice_denial
        self.grad_certificate=grad_certificate
        self.copy_identification=copy_identification
        self.verif_auth=verif_auth
        self.government_identification=government_identification
        self.identification_number=identification_number
        self.expiration_date=expiration_date
        self.certificate_maybe_issued=certificate_maybe_issued
        self.applicant_missing_documents=applicant_missing_documents
        self.name_inspector=name_inspector
        self.title_inspector=title_inspector
        self.date=date

class Final_Issuance(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    applic_id=db.Column(db.Integer, db.ForeignKey('application.id'))
    license_issued=db.Column(db.String(50))
    license_expdate=db.Column(db.DateTime)
    qualification=db.Column(db.String(50))
    qualif_expdate=db.Column(db.DateTime)
    authorization=db.Column(db.String(50))
    author_expdate=db.Column(db.DateTime)
    validation_certificate=db.Column(db.String(50))
    valid_expdate=db.Column(db.DateTime)
    official_name=db.Column(db.String(50))
    official_title=db.Column(db.String(50))
    final_date=db.Column(db.DateTime)

    def __init__(self,applic_id,license_issued,license_expdate,qualification,qualif_expdate,authorization,author_expdate,validation_certificate,valid_expdate,issuance_date,official_name,official_title,final_date):

        self.applic_id=applic_id
        self.license_issued=license_issued
        self.license_expdate=license_expdate
        self.qualification=qualification
        self.qualif_expdate=qualif_expdate
        self.authorization=authorization
        self.author_expdate=author_expdate
        self.validation_certificate=validation_certificate
        self.valid_expdate=valid_expdate
        self.issuance_date=issuance_date
        self.official_name=official_name
        self.official_title=official_title
        self.final_date=final_date


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

class Apply_form(db.Model):
    id=db.Column(db.Integer,primary_key=True)
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
