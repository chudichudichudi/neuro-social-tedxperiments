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
from .models import User, Experiment, ExperimentSerializer, Cronotipos
from .tools import requires_auth


@app.route('/')
def index():
    return render_template('index.html', total_users=User.query.count())


@app.route('/login')
def login():
    if current_user.is_authenticated():
        return redirect(redirect(request.args.get("next") or "/"))

    return render_template('login.html', form=LoginForm(), next=request.args.get("next"))


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
            flash('Cuenta creada correctamente!', 'info')
            return redirect(url_for(request.args.get('next') or 'index'))

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


# @app.route('/admin')
# @requires_auth
# def admin():
#     users = User.query.all()
#     return render_template('admin.html', users=users)


# @app.route('/admin/users/<user_id>', methods=['DELETE'])
# @requires_auth
# def delete_user(user_id):
#     user = User.query.get_or_404(user_id)
#     db.session.delete(user)
#     db.session.commit()
#     flash('User deleted successfully', 'info')
#     return redirect(url_for('admin'))


###Experiments Log

@app.route('/experiments/', methods=['GET'])
@cross_origin()
def get_all_experiments():
    experiments = Experiment.query.all()
    return jsonify({"experiments": ExperimentSerializer(experiments, many=True).data}), 200


@app.route('/experiments/create/', methods=['POST'])
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
    form = CronotiposForm()
    if form.validate_on_submit():
        return redirect('/cronotipos_results')
    return render_template('cronotipos.html', form=CronotiposForm())


@app.route('/cronotipos/results', methods=('GET','POST'))
@login_required
def cronotipos_results():
    form = CronotiposForm(csrf_enabled=False)
    crono = Cronotipos()

    if form.validate():
        crono.user_id = current_user.get_id()
        crono.pregunta_1 = form.pregunta_1.data['hours_field'] + u':' + form.pregunta_1.data['minutes_field']
        crono.pregunta_2 = form.pregunta_2.data['hours_field'] + u':' + form.pregunta_2.data['minutes_field']
        crono.pregunta_3 = form.pregunta_3.data['hours_field'] + u':' + form.pregunta_3.data['minutes_field']
        crono.pregunta_4 = form.pregunta_4.data
        crono.pregunta_5 = form.pregunta_5.data['hours_field'] + u':' + form.pregunta_5.data['minutes_field']
        crono.pregunta_6 = form.pregunta_6.data['hours_field'] + u':' + form.pregunta_6.data['minutes_field']
        crono.pregunta_7 = form.pregunta_7.data['hours_field'] + u':' + form.pregunta_7.data['minutes_field']
        crono.pregunta_8 = form.pregunta_8.data
        crono.pregunta_9 = form.pregunta_9.data['hours_field'] + u':' + form.pregunta_9.data['minutes_field']
        crono.pregunta_10 = form.pregunta_10.data['hours_field'] + u':' + form.pregunta_10.data['minutes_field']
        crono.pregunta_11 = form.pregunta_11.data
        crono.pregunta_12 = form.pregunta_12.data
        crono.pregunta_13 = form.pregunta_13.data
        crono.pregunta_14 = form.pregunta_14.data
        crono.pregunta_15 = form.pregunta_15.data
        crono.pregunta_16 = form.pregunta_16.data
        crono.pregunta_17 = form.pregunta_17.data

        crono.pregunta_18 = form.pregunta_18.data['hours_field'] + u':' + form.pregunta_18.data['minutes_field']

        crono.pregunta_19 = form.pregunta_19.data
        crono.pregunta_20 = form.pregunta_20.data
        crono.pregunta_21 = form.pregunta_21.data
        crono.pregunta_22 = form.pregunta_22.data
        crono.pregunta_23 = form.pregunta_23.data
        crono.pregunta_24 = form.pregunta_24.data
        crono.pregunta_25 = form.pregunta_25.data['hours_field'] + u':' + form.pregunta_25.data['minutes_field']
        crono.pregunta_26 = form.pregunta_26.data['hours_field'] + u':' + form.pregunta_26.data['minutes_field']
        crono.pregunta_27 = form.pregunta_27.data
        db.session.add(crono)
        db.session.commit()
        return render_template('cronotipos_results.html', crono_result=crono.process_data())
    print form.errors
    flash(u'Por favor completa todos los campos')
    return render_template('cronotipos.html', form=form)

@app.route('/consentimiento_cronotipos', methods=('GET', 'POST'))
@login_required
def consentimiento_cronotipos():
    return render_template('consentimiento_cronotipos.html')


#Circles
@app.route('/circles', methods=('GET', 'POST'))
@login_required
def circles():
    return redirect('http://circles-experiment.meteor.com?tedx_user_id=' + str(current_user.get_id()), 303)
