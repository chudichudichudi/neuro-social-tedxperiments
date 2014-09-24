# -*- coding: utf-8 -*-

from flask.ext.migrate import Migrate
from flask import redirect, url_for
from flask.ext.assets import Environment
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    login_user, core
from flask.ext.social import Social, SQLAlchemyConnectionDatastore, \
    login_failed
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from flask.ext.social.utils import get_connection_values_from_oauth_response
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

from .helpers import Flask
import uuid


app = Flask(__name__)
app.config.from_yaml(app.root_path)
app.wsgi_app = ProxyFix(app.wsgi_app)


db = SQLAlchemy(app)
webassets = Environment(app)
migrate = Migrate(app, db)

# Late import so modules can import their dependencies properly
from . import assets, models, views

admin = Admin(app, url='/its_a_secret/')
admin.add_view(models.CronotiposAdminView(models.Cronotipos, db.session))
admin.add_view(models.UsersAdminView(models.User, db.session))


from flask.ext.social.views import connect_handler

security_ds = SQLAlchemyUserDatastore(db, models.User, models.Role)
social_ds = SQLAlchemyConnectionDatastore(db, models.Connection)

from flask.ext.security import LoginForm

LoginForm.email.label = u'Dirección de Email'
LoginForm.password.label = u'Contraseña'

core._default_messages['LOGIN'] = ('Por favor ingresa tu usuario y clave.',
                                   'info')
app.security = Security(app, security_ds)
app.social = Social(app, social_ds)


class SocialLoginError(Exception):
    def __init__(self, provider):
        self.provider = provider


@app.before_first_request
def before_first_request():
    try:
        models.db.create_all()
    except Exception, e:
        app.logger.error(str(e))


@app.context_processor
def template_extras():
    return dict(
        google_analytics_id=app.config.get('GOOGLE_ANALYTICS_ID', None))


@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    connection_values = get_connection_values_from_oauth_response(provider,oauth_response)
    ds = app.security.datastore
    user = ds.create_user(email=str(uuid.uuid1()), password="123")
    ds.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    ds.commit()
    return redirect(url_for('index'))


@app.errorhandler(SocialLoginError)
def social_login_error(error):
    return redirect(
        url_for('register'))
