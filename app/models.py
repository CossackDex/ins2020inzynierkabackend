from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = "user_data_auth"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Boolean, nullable=False, default=False)
    superuser = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(256), nullable=False, unique=False)
    is_banned = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    survey_completed = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    force_password_change = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    created_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, role=False, superuser=False, **kwargs):
        self.username = kwargs['username']
        self.email = kwargs['email']
        self.password_hash = kwargs['password_hash']
        self.role = role
        self.superuser = superuser

    def __repr__(self):
        return '<User {}>'.format(self.username)


class UserSurvey(db.Model):
    __tablename__ = "users_sourvey"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data_auth.id'), unique=True, nullable=False)
    created_data = db.Column(db.DateTime, default=datetime.now)
    user_metadata = db.relationship('User', backref='user_survey')

    # programming languages
    java = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    python = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    js = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    csharp = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    cpp = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    go = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    r = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    swift = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    php = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    sql = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    # book topics
    webdev = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    machinelearning = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    database = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    algorithms = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    softwaredev = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    # prefered book length
    long = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    medium = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    short = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    length_dontcare = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    # publishers
    the_pragmatic_bookshelf = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    manning_publications = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    oreilly_media = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    peachpit = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    no_starch_press = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    packt_publishing = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    que = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    leanpub = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    publisher_dontcare = db.Column(db.Boolean, nullable=False, unique=False, default=False)

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id'].id
        self.java = kwargs['java'] if kwargs['java'] is not None else False
        self.python = kwargs['python'] if kwargs['python'] is not None else False
        self.js = kwargs['js'] if kwargs['js'] is not None else False
        self.csharp = kwargs['csharp'] if kwargs['csharp'] is not None else False
        self.cpp = kwargs['cpp'] if kwargs['cpp'] is not None else False
        self.go = kwargs['go'] if kwargs['go'] is not None else False
        self.r = kwargs['r'] if kwargs['r'] is not None else False
        self.swift = kwargs['swift'] if kwargs['swift'] is not None else False
        self.php = kwargs['php'] if kwargs['php'] is not None else False
        self.sql = kwargs['sql'] if kwargs['sql'] is not None else False
        # book topics
        self.webdev = kwargs['webdev'] if kwargs['webdev'] is not None else False
        self.machinelearning = kwargs['machinelearning'] if kwargs['machinelearning'] is not None else False
        self.database = kwargs['database'] if kwargs['database'] is not None else False
        self.algorithms = kwargs['algorithms'] if kwargs['algorithms'] is not None else False
        self.softwaredev = kwargs['softwaredev'] if kwargs['softwaredev'] is not None else False
        # prefered book length
        self.long = kwargs['long'] if 'long' in kwargs else False
        self.medium = kwargs['medium'] if 'medium' in kwargs else False
        self.short = kwargs['short'] if 'short' in kwargs else False
        self.length_dontcare = kwargs['length_dontcare'] if 'length_dontcare' in kwargs else False
        # publishers
        self.the_pragmatic_bookshelf = kwargs[
            'the_paragmatic_booksheld'] if 'the_paragmatic_booksheld' in kwargs else False
        self.manning_publications = kwargs['manning_publications'] if 'manning_publications' in kwargs else False
        self.oreilly_media = kwargs['oreilly_media'] if 'oreilly_media' in kwargs else False
        self.peachpit = kwargs['peachpit'] if 'peachpit' in kwargs else False
        self.no_starch_press = kwargs['no_starch_press'] if 'no_starch_press' in kwargs else False
        self.packt_publishing = kwargs['packt_publishing'] if 'packt_publishing' in kwargs else False
        self.que = kwargs['que'] if 'que' in kwargs else False
        self.leanpub = kwargs['leanpub'] if 'leanpub' in kwargs else False
        self.publisher_dontcare = kwargs['publisher_dontcare'] if 'publisher_dontcare' in kwargs else False


class Book(db.Model):
    __tablename__ = "book_data"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    pub_year = db.Column(db.Integer, unique=False, nullable=False)
    programming_language = db.Column(db.String(80), unique=False, nullable=False)
    publisher = db.Column(db.String(80), unique=False, nullable=False)
    topic = db.Column(db.String(80), unique=False, nullable=False)
    number_of_pages = db.Column(db.Integer, unique=False, nullable=False)
    length = db.Column(db.String(80), unique=False, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user_data_auth.id'), nullable=False)
    created_data = db.Column(db.DateTime, default=datetime.now)
    user_metadata = db.relationship('User', backref='book_data')
    likes = db.Column(db.Integer, unique=False, default=1)
    dislikes = db.Column(db.Integer, unique=False, default=1)
    ratio = db.Column(db.Float, unique=False, default=1)

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.author = kwargs['author']
        self.pub_year = kwargs['pub_year']
        self.programming_language = kwargs['programming_language']
        self.publisher = kwargs['publisher']
        self.topic = kwargs['topic']
        self.creator_id = kwargs['creator_id'].id
        self.number_of_pages = kwargs['number_of_pages']
        if int(self.number_of_pages) > 400:
            self.length = 'long'
        elif int(self.number_of_pages) > 200:
            self.length = 'medium'
        else:
            self.length = 'short'

    def like(self):
        self.likes += 1
        self.ratio = self.likes / self.dislikes
        return True

    def dislike(self):
        self.dislike += 1
        self.ratio = self.likes / self.dislikes
        return True
