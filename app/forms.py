# -*- coding: utf-8 -*-

from flask import current_app
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError
from wtforms.validators import Required, Email, Length, Regexp, EqualTo


class UniqueUser(object):
    def __init__(self, message="Usuario ya existente"):
        self.message = message

    def __call__(self, form, field):
        if current_app.security.datastore.find_user(email=field.data):
            raise ValidationError(self.message)


validators = {
    'email': [
        Required(),
        Email(),
        UniqueUser(message=u'El email está asociado con una cuenta existente.')
    ],
    'password': [
        Required(),
        Length(min=6, max=50),
        EqualTo('confirm', message=u'Las contraseñas deben coincidir.'),
        Regexp(r'[A-Za-z0-9@#$%^&+=]',
               message=u'La contraseña tiene que tener caracteres válidos')
    ]
}


class RegisterForm(Form):
    email = TextField('Email', validators['email'])
    password = PasswordField(u'Contraseña', validators['password'], )
    confirm = PasswordField(u'Confirmar contraseña')
