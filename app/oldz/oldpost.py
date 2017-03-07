from app import *
from app.model.model import *
from app.model.schema import *
from flask import jsonify,request
import datetime
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.controllers.controller import *



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
            type_demand=json_data["type_demand"],
            license=None,
            first_name=None,
            last_name=None,
            passport_id_Card=None,
            birthdate=None,
            birth_place=None,
            gender=None,
            address=None,
            resid_city=None,
            resid_state=None,
            resid_country=None,
            postal_code=None,
            phone=None,
            email=None,
            nationality=None,
            weight=None,
            height=None,
            hair=None,
            eyes=None,
            curr_lic_detention=None,
            lic_eversusp = None,
            type_license=None,
            lic_number=None,
            lic_issue_date=None,
            underst_french=None,
            underst_english=None,
            knowledge_test=None,
            test_applied_for = None,
            test_success = None,
            date_of_test_compl = None,
            skillTest=None,
            aircraft = None,
            time_in_aircraft =None,
            hours_of_flight=None,
            graduate_ato = None,
            name_institution = None,
            inst_city=None,
            inst_state=None,
            inst_country=None,
            ato_certiciate_no = None,
            grad_date=None,
            holder_foreign_lic=None,
            foreignlic_country=None,
            type_of_foreign_lic=None,
            lic_rating= None,
            military_competence = None,
            service=None,
            milit_grad_date=None,
            service_number = None,
            has_flied_10hours =None,
            last_flight_Check_date=None,
            final_certifying = None,
            regDate=None
            )
        db.session.add(appl)
        db.session.commit()
        result = appl_schema.dump(Application.query.get(appl.id))
        return jsonify({'Application':result.data})

    except:
        return jsonify({'Message':'0'})

#============================================================= POSTING A FINAL ISSUANCE ON APPLICATION ==============================
@app.route('/anac/final_iss/',methods=['POST'])
def fin():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= final_Issuance_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        fin = Final_Issuance(
            applic_id=json_data["applic_id"],
            license_issued=None,
            license_expdate=None,
            qualification=None,
            qualif_expdate=None,
            authorization=None,
            author_expdate=None,
            validation_certificate=None,
            valid_expdate=None,
            issuance_date=None,
            official_name=None,
            official_title=None,
            final_date=None,
            )
        db.session.add(fin)
        db.session.commit()
        result = final_Issuance_schema.dump(Final_Issuance.query.get(fin.id))
        return jsonify({'Issued License':result.data})

    except:
        return jsonify({'Message':'0'})


#============================================== POSTING A RECOMMANDATION ON APPLICATION =================================
@app.route('/anac/recomm/',methods=['POST'])
def recom():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= recomm_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        rec = Recommandation(
            applic_id=json_data["applic_id"],
            service_number=None,
            personally_instructed=None,
            date_of_instr=None,
            name_of_instr=None,
            license_number=None,
            expiration_date=None,
            approved_training_org=None,
            course_completed=None,
            endorsed_test=None,
            ato_date = None,
            ato_name=None,
            ato_certiciate_no=None,
            name_recommender = None,
            title_recommender = None,
            reviewed_theperson_applicant=None,
            knowledge_test=None,
            retake_of_passtest=None,
            retest_after_failure=None,
            reviewed_and_not_authorize=None,
            remarks=None,
            name_inspector=None,
            title_inspector=None,
            date_inspect=None,
            )
        db.session.add(rec)
        db.session.commit()
        result = recomm_schema.dump(Recommandation.query.get(rec.id))
        return jsonify({'Recommandation':result.data})

    except:
        return jsonify({'Message':'0'})

#======================================== POSTING A SKILL TEST REPORT ON APPLICATION ==========================
@app.route('/anac/skillt/',methods=['POST'])
def skil():
    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= skillTest_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        ski = SkillTest(
            applic_id=json_data["applic_id"],
            applicant_meets_reqs=None,
            applicant_and_results=None,
            approved=None,
            disapproved_notice=None,
            applicant_meets_linguistics=None,
            ling_french=None,
            ling_english=None,
            test_city=None,
            test_state=None,
            test_country=None,
            duration_of_test=None,
            examiner_number=None,
            licensefor_which_tested=None,
            date__test=None,
            name_examiner=None,
            )
        db.session.add(ski)
        db.session.commit()
        result = skillTest_schema.dump(SkillTest.query.get(ski.id))
        return jsonify({'Skill Test':result.data})

    except:
        return jsonify({'Message':'0'})


#================================================ POSTING ANAC REPORTS ON APPLICATION ===============================
@app.route('/anac/anac_report/',methods=['POST'])
def anac_rep():

    json_data=request.get_json()
    if not json_data:
        return jsonify({'Message':'No data provided'})
    data,errors= anac_Report_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    try:
        anac_re = Anac_Report(
            applic_id=json_data["applic_id"],
            accepted=None,
            rejected=None,
            renewal_license=None,
            reissue_license=None,
            issue_certificate=None,
            other=None,
            suspended_license=None,
            knowledge_test_report=None,
            skillTest_Report=None,
            notice_denial=None,
            grad_certificate=None,
            copy_identification=None,
            verif_auth=None,
            government_identification=None,
            identification_number=None,
            expiration_date=None,
            certificate_maybe_issued = None,
            applicant_missing_documents = None,
            name_inspector=None,
            title_inspector=None,
            date = None
            )
        db.session.add(anac_re)
        db.session.commit()
        result = anac_Report_schema.dump(Anac_Report.query.get(anac_re.id))
        return jsonify({'ANAC Report':result.data})

    except:
        return jsonify({'Message':'0'})
