# -*- coding: utf-8 -*-

from flask import current_app
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError, DateTimeField, RadioField
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
    ],
    'hora': [
        Required(),
        Length(min=4, max=4)
    ]
}


class RegisterForm(Form):
    email = TextField('Email', validators['email'])
    password = PasswordField(u'Contraseña', validators['password'], )
    confirm = PasswordField(u'Confirmar contraseña')


class CronotiposForm(Form):
    pregunta_1 = DateTimeField(u'1 - Me acuesto a las ... (Ejemplo 22:00)',
                               validators['hora'], format='%%H:%M')
    pregunta_2 = DateTimeField(u'2 - Necesito ... minutos para quedarme dormido'
                               u' (Ejemplo: 05 para 5 minutos)', format='%%M')
    pregunta_3 = DateTimeField(u'3 - Me despierto a las ... (Ejemplo 22:00)',
                               validators['hora'], format='%%H:%M')
    pregunta_4 = RadioField(u'4 - Indique qué tan buena es la calidad de su sueño en los días hábiles', choices=[('Muy mala 1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10 Excelente', '10')])
    
    pregunta_5 = DateTimeField(u'5 - Me acuesto a las ... (Ejemplo 22:00)', validators['hora'], format='%%H:%M')


    pregunta_6 = DateTimeField(u'6 - Necesito ... minutos para quedarme dormido (Ejemplo: 05 para 5 minutos)', format='%%M')


    pregunta_7 = DateTimeField(u'7 - Me despierto a las ... (Ejemplo 08:00)', validators['hora'], format='%%H:%M')

    pregunta_8 = RadioField(u'8 - Indique qué tan buena es la calidad de su sueño en los días libres', choices=[('Muy mala 1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10 Excelente', '10')])


    pregunta_9 = DateTimeField(u'9 - Si pudiera planear libremente su día ¿A qué hora se levantaría?', validators['hora'], format='%%H:%M')
    pregunta_10 = DateTimeField(u'10 - Si pudiera planear libremente su día ¿A qué hora se acostaría?', validators['hora'], format='%%H:%M')

    pregunta_11 = RadioField(u'11 - Si tiene que levantarse a una hora específica en la mañana ¿Cuánto depende de un reloj despertador?', choices=[('A', u'Nada'),(u'Poco', 'B'),(u'Bastante', 'C'),(u'Mucho', 'D')])

    pregunta_12 = RadioField(u'12 -  En un día con clima agradable, ¿Qué tan fácil le resulta levantarse en la mañana?', choices=[(u'Nada fácil', 'A'),(u'No muy fácil', 'B'),(u'Bastante fácil', 'C'),(u'Muy fácil', 'D')])

    pregunta_13 = RadioField(u'13 - ¿Qué tan atento y despejado se siente durante la primera media hora después de despertarse en la mañana? ', choices=[(u'Nada despejado', 'A'),(u'Poco despejado', 'B'),(u'Bastante despejado', 'C'),(u'Muy despejado', 'D')])

    pregunta_14 = RadioField(u'14 - ¿Qué tanto hambre siente durante la primera media hora después de despertarse en la mañana?', choices=[(u'Nada', 'A'),(u'Poco', 'B'),(u'Bastante', 'C'),(u'Muy', 'D')])
    pregunta_15 = RadioField(u'15 - ¿Cuánto cansancio siente durante la primera media hora después de despertarse en la mañana?', choices=[(u'Mucho', 'A'),(u'Bastante', 'B'),(u'Poco', 'C'),(u'Mucho', 'D')])

    pregunta_16 = RadioField(u'16 - Cuando no tiene nada que hacer al día siguiente ¿a qué hora se acuesta en comparación con lo que acostumbra?', choices=[(u'A la misma hora', 'A'),(u'Menos de 1 hora más tarde', 'B'),(u'Entre 1 y 2 horas más tarde', 'C'),(u'Más de 2 horas más tarde', 'D')])
    pregunta_17 = RadioField(u'17 - Un amigo lo invita a hacer ejercicio o practicar un deporte por la mañana, entre las 7 y las 8 de la mañana. ¿Cómo cree que sería su rendimiento? ', choices=[(u'Muy bueno', 'A'),(u'Razonable', 'B'),(u'Pobre', 'C'),(u'Malo', 'D')])
    pregunta_18 = DateTimeField(u'18- ¿A qué hora de la noche se siente tan cansado como para irse a dormir? (Ejemplo: 22:00)', validators['hora'], format='%%H:%M')
    pregunta_19 = RadioField(u'19 - Suponga que desea obtener los mejores resultados en un examen escrito, que va a ser mentalmente muy desgastante y durará 2 horas, pero Ud. puede elegir libremente el horario para hacerlo. ¿Cuál elegiría, pensando en aquel en que le va resultar más fácil responderlo? ', choices=[(u'8:00 -10:00', 'A'),(u'11:00 - 13:00', 'B'),(u'15:00 - 17:00 ', 'C'),(u'19:00 - 21:00', 'D')])
    pregunta_20 = RadioField(u'20- Si se fuera a dormir a las 23:00, ¿Qué nivel de cansancio o sueño sentiría?', choices=[(u'Nada', 'A'),(u'Poco', 'B'),(u'Bastante', 'C'),(u'Mucho', 'D')])
    pregunta_21 = RadioField(u'21 - Si por alguna razón Ud. se va a dormir algunas horas más tarde de lo habitual, pero al otro día no tiene necesidad de despertarse en el mismo horario de todos los días, ¿Qué le ocurriría?', choices=[(u'Se despertaría a la hora habitual y ya no dormiría', 'A'),(u'Se despertaría a la hora habitual y se sentiría somnoliento', 'B'),(u'Se despertaría a la hora habitual y se volvería a dormir inmediatamente', 'C'),(u'Se despertaría más tarde de lo habitual', 'D')])