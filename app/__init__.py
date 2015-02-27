# -*- coding: utf-8 -*-

from flask.ext.migrate import Migrate
from flask import redirect, url_for
from flask.ext.assets import Environment
from flask.ext.admin import Admin, AdminIndexView, expose
from flask.ext import login
from rq_dashboard import RQDashboard
from flask.ext.sqlalchemy import SQLAlchemy
from .helpers import Flask
from redis import Redis
from rq import Queue


class CustomAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('/'))
        return super(CustomAdminIndexView, self).index()


app = Flask(__name__)
app.config.from_yaml(app.root_path)

q = Queue(connection=Redis())

RQDashboard(app)

db = SQLAlchemy(app)
webassets = Environment(app)
migrate = Migrate(app, db)

# Late import so modules can import their dependencies properly
from . import models
admin = Admin(app, url='/its_a_secret')


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
