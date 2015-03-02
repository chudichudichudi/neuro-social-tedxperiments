# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, jsonify, send_file
from flask.ext.cors import cross_origin
import json
from . import app, db, q
from .models import Experiment, ExperimentSerializer, FileExperiment
from rq import Queue


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
    experiments = db.session.query(Experiment)\
        .filter(Experiment.experiment_name
                == experiment)
    def generate():
        for row in experiments:
            yield jsonify(ExperimentSerializer(row).data)


@app.route('/experiments/file/<experiment>', methods=['GET'])
@cross_origin(headers=['Content-Type'])
def get_experiment(experiment):
    experiments = db.session.query(Experiment)\
        .filter(Experiment.experiment_name
                == experiment)

    def generate():
        for row in experiments:
            yield jsonify(ExperimentSerializer(row).data)


# @app.route('/experiments/file/<experiment>', methods=['GET'])
# @cross_origin(headers=['Content-Type'])
# def get_experiment_file(experiment):
#     res = q.enqueue(generate_file, experiment)
#     return render_template("celery_tasks.html", experiment=experiment)

# def generate_file(experiment):
#     experiments = db.session.query(Experiment).filter(Experiment.experiment_name == experiment)

#     file_experiment = FileExperiment()
#     file_experiment.experiment_name = experiment
#     db.session.add(experiment)
#     db.session.commit()


# @app.route('/experiments/file/get/<file_id>', methods=['GET'])
# @cross_origin(headers=['Content-Type'])
# def download_file(experiment):
#     res = q.enqueue(generate_file, experiment)
#     return render_template("celery_tasks.html", experiment=experiment)
