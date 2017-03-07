from app import *
from app.model.model import *
from app.model.schema import *
from flask import jsonify,request
import datetime
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.controllers.controller import *




#=============================================== POSTING A USER, ADMIN OF THE SYSTEM ============================

@app.route('/anac/user_admin/',methods=['POST'])
def uadm():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= useradmin_schema.load(json_data)
    if errors:
        return jsonify(errors), 422
    username = get_username(data['first_name'],data["last_name"])
    pwd_hash = bcrypt.generate_password_hash(data['password'])

    try:
        admin = Admin_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=username,
            email=data["email"],
            password=pwd_hash,
            regDate=None
            )
        db.session.add(admin)
        db.session.commit()
        result = useradmin_schema.dump(Admin_user.query.get(admin.id))
        return jsonify({'auth': 1,'User':result.data})

    except:
        return jsonify({'auth': 0,})
#================================================== LOG IN ======================================================

@app.route('/anac/login/',methods=['POST'])
def login():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'Message':'No input data provided'}), 400
    data,errors=useradmin_schema.load(json_data)
    if errors:
        return jsonify(errors), 422
    username,password = data['username'],data['password']
    user=Admin_user.query.filter_by(username=username,password=password).first()
    if user is None:
        return jsonify({'Message':'0'})
    else:
        res=useradmin_schema.dump(Admin_user.query.get(user.id))
        return jsonify({'Message':'1','User':res.data})


@app.route('/anac/login1/',methods=['POST'])
def login1():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'Message':'No input data provided'}), 400
    data,errors = useradmin_schema.load(json_data)

    if errors:
        return jsonify(errors), 422

    username,password = data['username'],data['password']

    user = Admin_user.query.filter(Admin_user.username==username).first()

    try:
        pw_hash = bcrypt.check_password_hash(user.password, password)
        if pw_hash:
            result = useradmin_schema.dump(Admin_user.query.get(user.id))
            return jsonify({'auth': 1, 'user': result.data})
        else:
            return jsonify({'auth': 0})
    except AttributeError:
        return jsonify({'auth':2})


#========================================= POSTING AN DEMAND OR APPLICATION ======================

@app.route('/anac/appl/',methods=['POST'])
def application():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= appl_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        appl = Application(
            aeronefs = None
            personels = None
            raison_social = None
            addresse_sociale = None
            addresse_telephone = None
            addresse_electronique = None
            autre_appelation = None
            address_admin = None
            etablissement_sec = None
            type_exploitation = None
            date_commencemment = None
            regions_geographiques = None
            formations_proposees = None
            type_organisation = None
            nom_applicant = None
            prenom_applicant = None
            titre_applicant = None
            regDate = None

            )
        db.session.add(appl)
        db.session.commit()
        result = appl_schema.dump(Application.query.get(appl.id))
        return jsonify({'Application':result.data})

    except:
        return jsonify({'Message':'0'})

#==================================== AERONEFS =================================

@app.route('/anac/aero/',methods=['POST'])
def application():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= aero_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        aer = Aeronefs(

                applic_id = None
                type_aeronef = None
                marque = None
                model = None
                nationalite = None
                immatriculaton = None
                passagers = None
                capacite = None
                loue = None
                link = None

            )
        db.session.add(aer)
        db.session.commit()
        result = aero_schema.dump(Aeronefs.query.get(aer.id))
        return jsonify(result.data)

    except:
        return jsonify({'Message':'0'})

#=========================== Personnel =========================

@app.route('/anac/perso/',methods=['POST'])
def application():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= perso_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        aer = Personnel(

            applic_id=None
            names = None
            title = None
            telephone = None
            telecopieur = None
            email = None

            )
        db.session.add(aer)
        db.session.commit()
        result = aero_schema.dump(Personnel.query.get(aer.id))
        return jsonify(result.data)

    except:
        return jsonify({'Message':'0'})
