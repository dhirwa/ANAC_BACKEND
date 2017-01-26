from app import *
from app.model.model import *
from app.model.schema import *
from flask import request
from datetime import date
from datetime import time
from flask import jsonify
from datetime import datetime


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

#============================================== RECOMMANDATIONS ==============================

@app.route('/anac/recommandations')
def reco():
    reco = Recommandation.query.all()
    if reco:
        result = recomms_schema.dump(reco)
        return jsonify({'Recommandations':result.data})
    else:
        return jsonify({'message':'0'})

@app.route('/anac/recommandation/<int:rid>')
def rec(rid):
    rec = Application.query.get(rid)
    if rec:
        result = recomm_schema.dump(rec)
        return jsonify({'Recommandation':result.data})
    else:
        return jsonify({'message':'0'})

#============================================== SKILL TEST REPORT =============================

@app.route('/anac/skilltests')
def skill():
    skil = SkillTest.query.all()
    if skil:
        result = skillTests_schema.dump(skil)
        return jsonify({'Skill Tests':result.data})
    else:
        return jsonify({'message':'0'})


@app.route('/anac/skilltest/<int:skid>')
def skill(skid):
    skill=SkillTest.query.get(skid)
    if skill:
        result = skillTest_schema.dump(skill)
        return jsonify({'Skill Test Report':result.data})
    else:
        return jsonify({'message':'0'})

#============================================== ANAC REPORT =====================================

@app.route('/anac/anac_reports')
def anac_reps():
    reps = Anac_Report.query.all()
    if reps:
        result = anac_Reports_schema.dump(reps)
        return jsonify({'ANAC Reports':result.data})
    else:
        return jsonify({'message':'0'})


@app.route('/anac/anac_report/<int:arid>')
def anac_rep(arid):
    anac_rep=Anac_Report.query.get(arid)
    if anac_rep:
        result = anac_Report_schema.dump(anac_rep)
        return jsonify({'Anac Report':result.data})
    else:
        return jsonify({'Message':'0'})


#============================================ FINAL ISSUANCE =========================================

@app.route('/anac/final_issuances')
def finals():
    finals = Final_Issuance.query.all()
    if finals:
        result = final_Issuances_schema.dump(finals)
        return jsonify({'Issued Licences':result.data})
    else:
        return jsonify({'message':'0'})


@app.route('/anac/final_issuance/<int:fiid>')
def final(fiid):
    final=Final_Issuance.query.get(fiid)
    if fiid:
        result = final_Issuance_schema.dump(final)
        return jsonify({'Licence':result.data})
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
