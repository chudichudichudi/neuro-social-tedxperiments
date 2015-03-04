# -*- coding: utf-8 -*-
from datetime import datetime
from collections import defaultdict
from flask import render_template, redirect, request, current_app, session, \
    flash, jsonify, send_file
from flask.ext.security import LoginForm, current_user, login_required, \
    login_user, roles_required
import csv
import StringIO

from . import app, db
from .forms import CronotiposForm
from .models import  Cronotipos


@app.route('/')
def index():
    return redirect('/cronotipos')



#Cronotipos
@app.route('/cronotipos')
def cronotipos():
    form = CronotiposForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect('/cronotipos_results')
    return render_template('cronotipos.html', form=CronotiposForm())

@app.route('/cronotipos/csv')
def cronotipos_csv():
    buffer = StringIO.StringIO()
    outcsv = csv.writer(buffer)
    records = Cronotipos.query.all()
    columns_names = Cronotipos.__mapper__.columns

    lst_columns = []
    for column in columns_names:
        lst_columns.append(column.name)
    outcsv.writerow(lst_columns)

    for row in records:
        lst = []
        for column in columns_names:
            lst.append(getattr(row, column.name))
        outcsv.writerow(lst)
    buffer.seek(0)
    return send_file(buffer,
                     as_attachment=True,
                     attachment_filename='cronotipos.csv',
                     mimetype='text/csv')


@app.route('/cronotipos/results', methods=('GET', 'POST'))
def cronotipos_results():
    form = CronotiposForm(csrf_enabled=False)
    if form.validate():
        crono = Cronotipos()
        crono.user_id = current_user.get_id()
        crono.pregunta_1 = form.pregunta_1.data['hours_field'] + u':' + form.pregunta_1.data['minutes_field']
        #crono.pregunta_2 = form.pregunta_2.data['hours_field'] + u':' + form.pregunta_2.data['minutes_field']
        crono.pregunta_2 = form.pregunta_2.data
        crono.pregunta_3 = form.pregunta_3.data['hours_field'] + u':' + form.pregunta_3.data['minutes_field']
        crono.pregunta_4 = form.pregunta_4.data
        crono.pregunta_5 = form.pregunta_5.data['hours_field'] + u':' + form.pregunta_5.data['minutes_field']
        # crono.pregunta_6 = form.pregunta_6.data['hours_field'] + u':' + form.pregunta_6.data['minutes_field']
        crono.pregunta_6 = form.pregunta_6.data
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
        crono.result = crono.process_data()
        crono.result_type = crono.get_crono_type(crono.process_data())
        crono.date = datetime.now()
        db.session.add(crono)
        db.session.commit()
        return render_template('cronotipos_results.html',
                               crono_result=crono.get_crono_type_human(crono.process_data()),
                               crono_chart=crono_dict)
    flash(u'Por favor completa todos los campos')
    return render_template('cronotipos.html', form=form)


@app.route('/consentimiento_cronotipos', methods=('GET', 'POST'))
def consentimiento_cronotipos():
    return render_template('consentimiento_cronotipos.html')
