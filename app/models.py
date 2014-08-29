
from flask.ext.security import UserMixin, RoleMixin
from marshmallow import Serializer
from datetime import date, datetime, time, timedelta


from . import db


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                       db.ForeignKey('users.id')),
                       db.Column('role_id', db.Integer(),
                       db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):

    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    connections = db.relationship('Connection',
                                  backref=db.backref('user', lazy='joined'),
                                  cascade="all")


class Connection(db.Model):

    __tablename__ = "connections"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)


class Experiment(db.Model):
    __tablename__ = 'experiment'
    id = db.Column('id', db.Integer, primary_key=True)
    test_subject = db.Column(db.String(60))
    experiment_log = db.Column(db.String)
    experiment_name = db.Column(db.String)


class ExperimentSerializer(Serializer):
    class Meta:
        fields = ('id', 'test_subject', 'experiment_log', "experiment_name")


class Cronotipos(db.Model):
    __tablename__ = 'cronotipos'
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pregunta_1 = db.Column(db.String)
    pregunta_2 = db.Column(db.String)
    pregunta_3 = db.Column(db.String)
    pregunta_4 = db.Column(db.String)
    pregunta_5 = db.Column(db.String)
    pregunta_6 = db.Column(db.String)
    pregunta_7 = db.Column(db.String)
    pregunta_8 = db.Column(db.String)
    pregunta_9 = db.Column(db.String)
    pregunta_10 = db.Column(db.String)
    pregunta_11 = db.Column(db.String)
    pregunta_12 = db.Column(db.String)
    pregunta_13 = db.Column(db.String)
    pregunta_14 = db.Column(db.String)
    pregunta_15 = db.Column(db.String)
    pregunta_16 = db.Column(db.String)
    pregunta_17 = db.Column(db.String)
    pregunta_18 = db.Column(db.String)
    pregunta_19 = db.Column(db.String)
    pregunta_20 = db.Column(db.String)
    pregunta_21 = db.Column(db.String)
    pregunta_22 = db.Column(db.String)
    pregunta_23 = db.Column(db.String)
    pregunta_24 = db.Column(db.String)
    pregunta_25 = db.Column(db.String)
    pregunta_26 = db.Column(db.String)
    pregunta_27 = db.Column(db.String)

    @staticmethod
    def res_question_9(hs, mn):
        td_5_0 = timedelta(hours=5, minutes=0)
        td_6_30 = timedelta(hours=6, minutes=30)
        td_7_44 = timedelta(hours=7, minutes=44)
        td_7_45 = timedelta(hours=7, minutes=45)
        td_9_44 = timedelta(hours=9, minutes=44)
        td_9_45 = timedelta(hours=9, minutes=45)
        td_10_59 = timedelta(hours=10, minutes=59)
        td_11_0 = timedelta(hours=11, minutes=0)
        td_12_0 = timedelta(hours=12, minutes=0)




# 1. 5 a 6.29 5
#     6.30 a 7.44 4
#     7.45 a  9.44    3
#     9.45 a 10.59    2
#     11 a 12 1


    def process_data(self):
        result = 0
        hs_9, min_9 = self.pregunta_9.split(u';')
        hs_9 = 
        

        return 1
