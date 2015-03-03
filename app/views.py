# -*- coding: utf-8 -*-
from datetime import datetime
from collections import defaultdict
from flask import render_template, redirect, request, current_app, session, \
    flash, jsonify, send_file, Response, stream_with_context, json
from flask.ext.security import LoginForm, current_user, login_required, \
    login_user, roles_required
from flask.ext.social.utils import get_provider_or_404
from flask.ext.social.views import connect_handler
from flask.ext.cors import cross_origin

import csv
import StringIO
import io

from . import app, db
from .forms import RegisterForm, CronotiposForm
from .models import User, Experiment, ExperimentSerializer, Cronotipos
from .tools import UnicodeWriter

@app.route('/experiments/', methods=['GET'])
@cross_origin(headers=['Content-Type'])
def get_all_experiments():
    experiments = Experiment.query.all()
    return jsonify({"experiments": ExperimentSerializer(experiments, many=True).data}), 200


@app.route('/experiments/create/', methods=['POST'])
@cross_origin(headers=['Content-Type'])
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
@cross_origin(headers=['Content-Type'])
def get_log(id):
    experiment = Experiment.query.get(id)
    return jsonify({"experiments": ExperimentSerializer(experiment).data}), 200


@app.route('/experiments/append/', methods=['POST'])
@cross_origin(headers=['Content-Type'])
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
@cross_origin(headers=['Content-Type'])
def get_experiment(experiment):
    experiments = db.session.query(Experiment).filter(Experiment.experiment_name == experiment)
    res = {"experiments": [exp.serialize for exp in experiments]}
    return jsonify(res), 200


@app.route('/experiments/file/<experiment>', methods=['GET'])
@cross_origin(headers=['Content-Type'])
def get_experiment_file(experiment):
    experiments = db.session.query(Experiment).filter(Experiment.experiment_name == experiment)

    def generate():
        yield '{  "experiments": ['
        for exp in experiments[:-1]:
            yield json.dumps(exp.serialize) + ','
        yield json.dumps(experiments[-1].serialize)
        yield ']}'

    return Response(stream_with_context(generate()), mimetype='text/csv')
