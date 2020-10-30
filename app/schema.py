from . import ma
from .models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    role = ma.auto_field()
    superuser = ma.auto_field()
    is_banned = ma.auto_field()
    force_password_change = ma.auto_field()
    created_date = ma.auto_field()