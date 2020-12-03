from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from ..decorators import *
from ..models import *
from ..schema import UserSurveySchema

survey_bp = Blueprint('survey_bp', __name__)


@survey_bp.route('/dashboard/surveys', methods=['GET'])
@required_login
@required_admin
def surveys_get(user=None):
    surveys_list = UserSurvey.query.all()
    if surveys_list is None:
        return jsonify(message='No surveys in database'), 204
    survey_schema = UserSurveySchema(many=True)
    return jsonify({'books': survey_schema.dump(surveys_list)}), 200


@survey_bp.route('/dashboard/surveys', methods=['POST'])
@required_login
def survey_post(user=None):
    data = request.get_json()
    data['user_id'] = user
    new_survey = UserSurvey(**data)
    db.session.add(new_survey)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="db error", error_message=str(e.orig)), 404
    user.survey_completed = True
    # user.survey_id = new_survey.id
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(message="db error", error_message=str(e.orig)), 404
    return jsonify(message='survey for user - {} has been created'.format(user.username)), 200


@survey_bp.route('/dashboard/survey', methods=['GET', 'PUT', 'DELETE'])
@required_login
def survey_manage(user=None):
    if request.method == "PUT":

        old_survey = UserSurvey.query.filter_by(user_id=user.id).first()
        if old_survey is None:
            return jsonify(message="survey doesn't exist in db"), 404
        data = request.get_json()
        db.session.delete(old_survey)
        try:
            db.session.commit()
        except IntegrityError as e:
            return jsonify(message="db error", error_message=str(e.orig)), 404
        data['user_id'] = user
        new_survey = UserSurvey(**data)
        db.session.add(new_survey)
        try:
            db.session.commit()
        except IntegrityError as e:
            return jsonify(message="db error", error_message=str(e.orig)), 404
        return jsonify(message='survey for user - {} has been created'.format(user.username)), 200
    elif request.method == "DELETE":
        survey = UserSurvey.query.filtery_by(user_id=user.id).first()
        if survey is None:
            return jsonify(message="survey doesn't exist in db"), 404
        db.session.delete(survey)
        try:
            db.session.commit()
        except IntegrityError as e:
            return jsonify(message="db error", error_message=str(e.orig)), 404
        return jsonify(message="survey deleted"), 200
    else:
        survey = UserSurvey.query.filtery_by(user_id=user.id).first()
        if survey is None:
            return jsonify(message="survey doesn't exist in db"), 404
        survey_schema = UserSurveySchema()
        return jsonify({survey_schema.dump(survey)}), 200
