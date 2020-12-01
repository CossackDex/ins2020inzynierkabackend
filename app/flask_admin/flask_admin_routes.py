from flask import Blueprint
from app import db, flask_adminer
from app.models import User, UserSurvey, Book
from flask_admin.contrib.sqla import ModelView

flask_admin_bp = Blueprint('flask_admin_bp', __name__)

flask_adminer.add_view(ModelView(User, db.session))
flask_adminer.add_view(ModelView(UserSurvey, db.session))
flask_adminer.add_view(ModelView(Book, db.session))
