from flask.ext.security import UserMixin, RoleMixin
from marshmallow import Serializer
from datetime import timedelta
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

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

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean())
    name = db.Column(db.String(255))
    twitter_handle = db.Column(db.String(255))
    work = db.Column(db.String(255))
    study = db.Column(db.String(255))
    age = db.Column(db.String(255))
    sex = db.Column(db.String(255))
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

    def __str__(self):
        return self.email


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


class CustomModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated()


class UsersAdminView(CustomModelView):
    column_list = ('id',
                   'email',
                   'name',
                   'twitter_handle',
                   'work',
                   'study',
                   'age',
                   'sex',
                   'roles',
                   'last_login_at')
    column_sortable_list = (('id', User.id), ('last_login_at', User.last_login_at))


class CronotiposAdminView(CustomModelView):
    column_list = ('id',
                   'user_id',
                   'pregunta_1',
                   'pregunta_2',
                   'pregunta_3',
                   'pregunta_4',
                   'pregunta_5',
                   'pregunta_6',
                   'pregunta_7',
                   'pregunta_8',
                   'pregunta_9',
                   'pregunta_10',
                   'pregunta_11',
                   'pregunta_12',
                   'pregunta_13',
                   'pregunta_14',
                   'pregunta_15',
                   'pregunta_16',
                   'pregunta_17',
                   'pregunta_18',
                   'pregunta_19',
                   'pregunta_20',
                   'pregunta_21',
                   'pregunta_22',
                   'pregunta_23',
                   'pregunta_24',
                   'pregunta_25',
                   'pregunta_26',
                   'pregunta_27',
                   'result',
                   'result_type',
                   'date')


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
    result = db.Column(db.String)
    result_type = db.Column(db.String)
    date = db.Column(db.DateTime)

    def get_crono_type_human(self, crono_result):
        if crono_result >= 70 and crono_result <= 86:
            return 'Definitivamente Matutino'
        elif crono_result >= 59 and crono_result <= 69:
            return 'Moderadamente Matutino'
        elif crono_result >= 42 and crono_result <= 58:
            return 'Intermedio'
        elif crono_result >= 31 and crono_result <= 41:
            return 'Moderadamente Nocturno'
        elif crono_result >= 16 and crono_result <= 30:
            return 'Definitivamente Nocturno'
        else:
            return 'Fuera De Escala'

    def get_crono_type(self, crono_result):
        if crono_result >= 70 and crono_result <= 86:
            return 'definitivamente_matutino'
        elif crono_result >= 59 and crono_result <= 69:
            return 'moderadamente_matutino'
        elif crono_result >= 42 and crono_result <= 58:
            return 'intermedio'
        elif crono_result >= 31 and crono_result <= 41:
            return 'moderadamente_nocturno'
        elif crono_result >= 16 and crono_result <= 30:
            return 'definitivamente_nocturno'
        else:
            return 'fuera_de_escala'

    @staticmethod
    def res_question_9(hs, mn):
        t0 = timedelta(hours=hs, minutes=mn)

        if t0 >= timedelta(hours=5, minutes=0) and \
           t0 <= timedelta(hours=6, minutes=29):
            return 5

        if t0 >= timedelta(hours=6, minutes=30) and \
           t0 <= timedelta(hours=7, minutes=44):
            return 4

        if t0 >= timedelta(hours=7, minutes=45) and \
           t0 <= timedelta(hours=9, minutes=44):
            return 3

        if t0 >= timedelta(hours=9, minutes=45) and \
           t0 <= timedelta(hours=10, minutes=59):
            return 2

        if t0 >= timedelta(hours=11, minutes=0) and \
           t0 <= timedelta(hours=13, minutes=0):
            return 1
        return 0

    @staticmethod
    def res_question_10(hs, mn):
        if hs < 5:
            t0 = timedelta(hours=hs + 24, minutes=mn)
        else:
            t0 = timedelta(hours=hs, minutes=mn)

        if t0 >= timedelta(hours=20, minutes=0) and \
           t0 <= timedelta(hours=20, minutes=59):
            return 5

        if t0 >= timedelta(hours=21, minutes=0) and \
           t0 <= timedelta(hours=22, minutes=14):
            return 4

        if t0 >= timedelta(hours=22, minutes=15) and \
           t0 <= timedelta(days=1, hours=0, minutes=29):
            return 3

        if t0 >= timedelta(days=1, hours=0, minutes=30) and \
           t0 <= timedelta(days=1, hours=1, minutes=44):
            return 2

        if t0 >= timedelta(days=1, hours=1, minutes=45) and \
           t0 <= timedelta(days=1, hours=4, minutes=0):
            return 1
        return 0

    @staticmethod
    def res_question_18(hs, mn):
        if hs < 5:
            t0 = timedelta(hours=hs + 24, minutes=mn)
        else:
            t0 = timedelta(hours=hs, minutes=mn)

        if t0 >= timedelta(hours=20, minutes=0) and \
           t0 <= timedelta(hours=20, minutes=59):
            return 5

        if t0 >= timedelta(hours=21, minutes=0) and \
           t0 <= timedelta(hours=22, minutes=14):
            return 4

        if t0 >= timedelta(hours=22, minutes=15) and \
           t0 <= timedelta(days=1, hours=0, minutes=44):
            return 3

        if t0 >= timedelta(days=1, hours=0, minutes=45) and \
           t0 <= timedelta(days=1, hours=1, minutes=59):
            return 2

        if t0 >= timedelta(days=1, hours=2, minutes=0) and \
           t0 <= timedelta(days=1, hours=4, minutes=0):
            return 1
        return 0

    @staticmethod
    def res_question_25(hs, mn):
        if hs < 10:
            t0 = timedelta(hours=hs + 24, minutes=mn)
        else:
            t0 = timedelta(hours=hs, minutes=mn)

        if t0 >= timedelta(hours=11, minutes=0) and \
           t0 <= timedelta(hours=21, minutes=59):
            return 1

        if t0 >= timedelta(hours=22, minutes=0) and \
           t0 <= timedelta(days=1, hours=1, minutes=59):
            return 5

        if t0 >= timedelta(days=1, hours=2, minutes=0) and \
           t0 <= timedelta(days=1, hours=2, minutes=59):
            return 4

        if t0 >= timedelta(days=1, hours=3, minutes=0) and \
           t0 <= timedelta(days=1, hours=7, minutes=59):
            return 3

        if t0 >= timedelta(days=1, hours=8, minutes=0) and \
           t0 <= timedelta(days=1, hours=11, minutes=0):
            return 2
        return 0

    @staticmethod
    def res_question_26(hs, mn):
        t0 = timedelta(hours=hs, minutes=mn)

        if t0 >= timedelta(hours=0, minutes=0) and \
           t0 <= timedelta(hours=2, minutes=59):
            return 1

        if t0 >= timedelta(hours=3, minutes=0) and \
           t0 <= timedelta(hours=5, minutes=59):
            return 5

        if t0 >= timedelta(hours=6, minutes=0) and \
           t0 <= timedelta(hours=8, minutes=59):
            return 4

        if t0 >= timedelta(hours=9, minutes=0) and \
           t0 <= timedelta(hours=14, minutes=59):
            return 3

        if t0 >= timedelta(hours=15, minutes=0) and \
           t0 <= timedelta(hours=19, minutes=59):
            return 2

        if t0 >= timedelta(hours=20, minutes=0) and \
           t0 <= timedelta(days=1, hours=0, minutes=0):
            return 1
        return 0

    @staticmethod
    def res_question_abcd_4321(option):
        if u'A' == option:
            return 4
        if u'B' == option:
            return 3
        if u'C' == option:
            return 2
        if u'D' == option:
            return 1

    @staticmethod
    def res_question_abcd_1234(option):
        if u'A' == option:
            return 1
        if u'B' == option:
            return 2
        if u'C' == option:
            return 3
        if u'D' == option:
            return 4

    @staticmethod
    def res_question_19(option):
        if u'A' == option:
            return 6
        if u'B' == option:
            return 4
        if u'C' == option:
            return 2
        if u'D' == option:
            return 0

    @staticmethod
    def res_question_20(option):
        if u'A' == option:
            return 0
        if u'B' == option:
            return 2
        if u'C' == option:
            return 3
        if u'D' == option:
            return 5

    @staticmethod
    def res_question_27(option):
        if u'A' == option:
            return 6
        if u'B' == option:
            return 4
        if u'C' == option:
            return 2
        if u'D' == option:
            return 0

    def process_data(self):
        result = 0
        hs_9, min_9 = self.pregunta_9.split(u':')
        result += Cronotipos.res_question_9(int(hs_9), int(min_9))

        hs_10, min_10 = self.pregunta_10.split(u':')
        result += Cronotipos.res_question_10(int(hs_10), int(min_10))

        result += Cronotipos.res_question_abcd_4321(self.pregunta_11)
        result += Cronotipos.res_question_abcd_1234(self.pregunta_12)
        result += Cronotipos.res_question_abcd_1234(self.pregunta_13)
        result += Cronotipos.res_question_abcd_1234(self.pregunta_14)
        result += Cronotipos.res_question_abcd_1234(self.pregunta_15)
        result += Cronotipos.res_question_abcd_4321(self.pregunta_16)
        result += Cronotipos.res_question_abcd_4321(self.pregunta_17)

        hs_18, min_18 = self.pregunta_18.split(u':')
        result += Cronotipos.res_question_18(int(hs_18), int(min_18))
        result += Cronotipos.res_question_19(self.pregunta_19)
        result += Cronotipos.res_question_20(self.pregunta_20)
        result += Cronotipos.res_question_abcd_4321(self.pregunta_21)
        result += Cronotipos.res_question_abcd_1234(self.pregunta_22)
        result += Cronotipos.res_question_abcd_4321(self.pregunta_23)
        result += Cronotipos.res_question_abcd_1234(self.pregunta_24)

        hs_25, min_25 = self.pregunta_25.split(u':')
        result += Cronotipos.res_question_25(int(hs_25), int(min_25))

        hs_26, min_26 = self.pregunta_26.split(u':')
        result += Cronotipos.res_question_26(int(hs_26), int(min_26))

        result += Cronotipos.res_question_27(self.pregunta_27)
        return result
