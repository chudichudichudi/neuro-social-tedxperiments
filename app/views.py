from flask import render_template, redirect, request, current_app, session, \
    flash, url_for, jsonify
from flask.ext.security import LoginForm, current_user, login_required, \
    login_user
from flask.ext.social.utils import get_provider_or_404
from flask.ext.social.views import connect_handler
from flask.ext.cors import cross_origin
import json

from . import app, db
from .forms import RegisterForm, CronotiposForm
from .models import User, Experiment, ExperimentSerializer
from .tools import requires_auth


@app.route('/')
def index():
    return render_template('index.html', total_users=User.query.count())


@app.route('/login')
def login():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    return render_template('login.html', form=LoginForm())


@app.route('/register', methods=['GET', 'POST'])
@app.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    form = RegisterForm()

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    if form.validate_on_submit():
        ds = current_app.security.datastore
        user = ds.create_user(email=form.email.data,
                              password=form.password.data)
        ds.commit()

        # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
        connection_values = session.pop('failed_login_connection', None)

        if connection_values:
            connection_values['user_id'] = user.id
            connect_handler(connection_values, provider)

        if login_user(user):
            ds.commit()
            flash('Account created successfully', 'info')
            return redirect(url_for('profile'))

        return render_template('thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('register.html',
                           form=form,
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                    twitter_conn=current_app.social.twitter.get_connection(),
                    facebook_conn=current_app.social.facebook.get_connection())


@app.route('/admin')
@requires_auth
def admin():
    users = User.query.all()
    return render_template('admin.html', users=users)


@app.route('/admin/users/<user_id>', methods=['DELETE'])
@requires_auth
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'info')
    return redirect(url_for('admin'))


###Experiments Log

@app.route('/experiments/', methods=['GET'])
@cross_origin()
def get_all_experiments():
    experiments = Experiment.query.all()
    return jsonify({"experiments": ExperimentSerializer(experiments, many=True).data}), 200


@app.route('/experiments/create', methods=['POST'])
@cross_origin()
def create_log():
    if not request.json or not 'test_subject' in request.json \
            or not 'experiment_name' in request.json:
        return ("error, missing parameter (test_subject, experiment_name,"
                " experiment_log optional) or not json"), 400
    test_subject = request.json['test_subject'] or 'nn'
    experiment_name = request.json['experiment_name'] or ''
    experiment = Experiment()
    experiment.test_subject = test_subject
    experiment.experiment_name = experiment_name
    if 'experiment_log' in request.json:
        experiment_log = request.json['experiment_log']
    else:
        experiment_log = '[]'
    experiment.experiment_log = experiment_log
    db.session.add(experiment)
    db.session.commit()
    return str(experiment.id), 201


@app.route('/experiments/log/<int:id>', methods=['GET'])
@cross_origin()
def get_log(id):
    experiment = Experiment.query.get(id)
    return jsonify({"experiments": ExperimentSerializer(experiment).data}), 200


@app.route('/experiments/append/', methods=['POST'])
@cross_origin()
def append_log():
    if not request.json or not 'id' in request.json \
            or not 'experiment_log' in request.json:
        return "error, missing parameter (id, log) or not json", 400
    experiment = Experiment.query.get(request.json['id'])
    new_log = json.loads(experiment.experiment_log)
    new_log.append(request.get_json()['experiment_log'])
    experiment.experiment_log = json.dumps(new_log)
    db.session.commit()
    return "ok", 200


@app.route('/experiments/<experiment>', methods=['GET'])
@cross_origin()
def get_experiment(experiment):
    experiments = db.session.query(Experiment)\
        .filter(Experiment.experiment_name
                == experiment)
    return jsonify({"experiments":
                    ExperimentSerializer(experiments, many=True).data}), 200


#Metacog
@app.route('/metacognition')
@login_required
def metacog_html():
    return app.send_static_file('metacognition/metacog.html')


@app.route('/metacog.js')
@login_required
def metacog_js():
    return app.send_static_file('metacognition/metacog.js')


#Cronotipos
@app.route('/cronotipos')
@login_required
def cronotipos():
    return render_template('cronotipos.html', form=CronotiposForm())
