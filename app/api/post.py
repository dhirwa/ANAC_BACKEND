from app import *
from app.model.model import *
from app.model.schema import *
from flask import jsonify,request,json
import datetime
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.controllers.controller import *

#============================================= APPLICATION ======================

@app.route('/anac/appl/',methods=['POST'])
def application():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= appl_schema.load(json_data)
    if errors:
        return jsonify(errors), 422
    datas = json.dumps(json_data["data"])
    try:
        appl = Application(
            data = datas,
            regDate=None
            )
        db.session.add(appl)
        db.session.commit()
        result = appl_schema.dump(Application.query.get(appl.id))
        return jsonify({'Application':result.data})

    except:
        return jsonify({'Message':'0'})


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
