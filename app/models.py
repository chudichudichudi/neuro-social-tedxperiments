from marshmallow import Serializer
import datetime

from . import db


class Experiment(db.Model):
    __tablename__ = 'experiment'
    id = db.Column('id', db.Integer, primary_key=True)
    test_subject = db.Column(db.String(60))
    experiment_log = db.Column(db.String)
    experiment_name = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class ExperimentSerializer(Serializer):
    class Meta:
        fields = ('id', 'test_subject', 'experiment_log',
                  "experiment_name", "created_date")


class FileExperiment(db.Model):
    __tablename__ = 'file_experiment'
    id = db.Column('id', db.Integer, primary_key=True)
    experiment_name = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
