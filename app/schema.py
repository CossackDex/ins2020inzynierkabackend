from . import ma
from .models import User, UserSurvey, Book


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


class UserSurveySchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserSurvey

    id = ma.auto_field()
    user_id = ma.auto_field()
    created_data = ma.auto_field()
    java = ma.auto_field()
    python = ma.auto_field()
    js = ma.auto_field()
    csharp = ma.auto_field()
    cpp = ma.auto_field()
    go = ma.auto_field()
    r = ma.auto_field()
    swift = ma.auto_field()
    php = ma.auto_field()
    sql = ma.auto_field()
    webdev = ma.auto_field()
    machinelearning = ma.auto_field()
    database = ma.auto_field()
    algorithms = ma.auto_field()
    softwaredev = ma.auto_field()
    long = ma.auto_field()
    medium = ma.auto_field()
    short = ma.auto_field()
    length_dontcare = ma.auto_field()
    the_pragmatic_bookshelf = ma.auto_field()
    manning_publications = ma.auto_field()
    oreilly_media = ma.auto_field()
    peachpit = ma.auto_field()
    no_starch_press = ma.auto_field()
    packt_publishing = ma.auto_field()
    que = ma.auto_field()
    leanpub = ma.auto_field()
    publisher_dontcare = ma.auto_field()


class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book

    id = ma.auto_field()
    title = ma.auto_field()
    author = ma.auto_field()
    pub_year = ma.auto_field()
    programming_language = ma.auto_field()
    publisher = ma.auto_field()
    topic = ma.auto_field()
    number_of_pages = ma.auto_field()
    length = ma.auto_field()
    creator_id = ma.auto_field()
    created_data = ma.auto_field()
    likes = ma.auto_field()
    dislikes = ma.auto_field()
    ratio = ma.auto_field()
