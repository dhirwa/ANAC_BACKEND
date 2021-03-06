from app import *
from app.model.model import *
from app.model.schema import *
from flask import request
from datetime import date
from datetime import time
from flask import jsonify
from datetime import datetime
from app.controllers.controller import *


@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404: Page not found, Please check ur route well.'

#============================================= APPLICATIONS =================================

@app.route('/anac/applications')
def appls():
    appls = Application.query.all()
    if appls:
        result = appls_schema.dump(appls)
        return jsonify({'Appplications':result.data})
    else:
        return jsonify({'message':'0'})


@app.route('/anac/applications/<int:aid>')
def appl(aid):
    appl = Application.query.get(aid)
    if appl:
        result = appl_schema.dump(appl)
        return jsonify({'Application':result.data})
    else:
        return jsonify({'message':'0'})

#============================================= ADMIN USERS ===========================================

@app.route('/anac/admin_users')
def admins():
    adms=Admin_user.query.all()
    if adms:
        result = useradmins_schema.dump(adms)
        return jsonify({'Admins':result.data})
    else:
        return jsonify({'Message':'0'})

@app.route('/anac/admin_user/<int:uaid>')
def admi(uaid):
    adms=Admin_user.query.get(uaid)
    if adms:
        result = useradmin_schema.dump(adms)
        return jsonify({'User Admins':result.data})
    else:
        return jsonify({'Message':'0'})
