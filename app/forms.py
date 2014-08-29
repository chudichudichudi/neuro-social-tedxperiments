# -*- coding: utf-8 -*-

from flask import current_app
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError, \
    RadioField, FormField, SelectField, Form as wtfForm
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


class HourForm(wtfForm):
    hour_choices = [(unicode(x), unicode(x)) for x in range(0, 24)]
    minute_choices = [(unicode(x), unicode(x)) for x in range(0, 60)]
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta9(wtfForm):
    hour_choices = [(unicode(x), unicode(x)) for x in range(5, 13)]
    minute_choices = [(unicode(x), unicode(x)) for x in range(0, 60)]
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta10(wtfForm):
    hour_choices = [(u'20', u'20'), (u'21', u'21'), (u'22', u'22'),
                    (u'23', u'23'), (u'0', u'0'), (u'1', u'1'),
                    (u'2', u'2'), (u'3', u'3')]
    minute_choices = [(unicode(x), unicode(x)) for x in range(0, 60)]
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)

class HourFormPregunta18(wtfForm):
    hour_choices = [(u'20', u'20'), (u'21', u'21'), (u'22', u'22'),
                    (u'23', u'23'), (u'0', u'0'), (u'1', u'1'),
                    (u'2', u'2'), (u'3', u'3')]
    minute_choices = [(unicode(x), unicode(x)) for x in range(0, 60)]
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)



class CronotiposForm(Form):
    pregunta_1 = FormField(HourForm, label=u'1 - Me acuesto a las ... (Ejemplo 22:00)')

    pregunta_2 = FormField(HourForm, label=u'2 - Necesito ... minutos para quedarme dormido')

    pregunta_3 = FormField(HourForm, label=u'3 - Me despierto a las ... (Ejemplo 22:00)')

    pregunta_4 = RadioField(u'4 - Indique qué tan buena es la calidad de su sueño en los días hábiles (Ejemplo: 1 Muy Mala, 10 Excelente)', choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')])

    pregunta_5 = FormField(HourForm, label=u'5 - Me acuesto a las ... (Ejemplo 22:00)')
    pregunta_6 = FormField(HourForm, label=u'6 - Necesito ... minutos para quedarme dormido (Ejemplo: 05 para 5 minutos)')
    pregunta_7 = FormField(HourForm, label=u'7 - Me despierto a las ... (Ejemplo 08:00)')

    pregunta_8 = RadioField(u'8 - Indique qué tan buena es la calidad de su sueño en los días libres (Ejemplo: 1 Muy Mala, 10 Excelente)',
                            choices=[('1', '1'),
                                     ('2', '2'),
                                     ('3', '3'),
                                     ('4', '4'),
                                     ('5', '5'),
                                     ('6', '6'),
                                     ('7', '7'),
                                     ('8', '8'),
                                     ('9', '9'),
                                     ('10', '10')])

    pregunta_9 = FormField(HourFormPregunta9,
                           label=u'9 - Si pudiera planear libremente su día ¿A qué hora se levantaría?')

    pregunta_10 = FormField(HourFormPregunta10,
                            label=u'10 - Si pudiera planear libremente su día ¿A qué hora se acostaría?')


    pregunta_11 = RadioField(u'11 - Si tiene que levantarse a una hora específica en la mañana ¿Cuánto depende de un reloj despertador?', choices=[('A', u'Nada'),('B', u'Poco'),('C', u'Bastante'),('D', u'Mucho')])

    pregunta_12 = RadioField(u'12 -  En un día con clima agradable, ¿Qué tan fácil le resulta levantarse en la mañana?',
                             choices=[('A', u'Nada fácil'),
                                      ('B', u'No muy fácil'),
                                      ('C', u'Bastante fácil'),
                                      ('D', u'Muy fácil')])

    pregunta_13 = RadioField(u'13 - ¿Qué tan atento y despejado se siente durante la primera media hora después de despertarse en la mañana? ',
                             choices=[('A', u'Nada despejado'),
                                      ('B', u'Poco despejado'),
                                      ('C', u'Bastante despejado'),
                                      ('D', u'Muy despejado')])

    pregunta_14 = RadioField(u'14 - ¿Qué tanto hambre siente durante la primera media hora después de despertarse en la mañana?',
                             choices=[('A', u'Nada'),
                                      ('B', u'Poco'),
                                      ('C', u'Bastante'),
                                      ('D', u'Muy')])
    pregunta_15 = RadioField(u'15 - ¿Cuánto cansancio siente durante la primera media hora después de despertarse en la mañana?',
                             choices=[('A', u'Mucho'),
                                      ('B', u'Bastante'),
                                      ('C', u'Poco'),
                                      ('D', u'Mucho')])

    pregunta_16 = RadioField(u'16 - Cuando no tiene nada que hacer al día siguiente ¿a qué hora se acuesta en comparación con lo que acostumbra?',
                             choices=[('A', u'A la misma hora'),
                                      ('B', u'Menos de 1 hora más tarde'),
                                      ('C', u'Entre 1 y 2 horas más tarde'),
                                      ('D', u'Más de 2 horas más tarde')])
    pregunta_17 = RadioField(u'17 - Un amigo lo invita a hacer ejercicio o practicar un deporte por la mañana, entre las 7 y las 8 de la mañana. ¿Cómo cree que sería su rendimiento? ',
                             choices=[('A', u'Muy bueno'),
                                      ('B', u'Razonable'),
                                      ('C', u'Pobre'),
                                      ('D', u'Malo')])

    pregunta_18 = FormField(HourFormPregunta18,
                           label=u'18- ¿A qué hora de la noche se siente tan cansado como para irse a dormir? (Ejemplo: 22:00)')

    pregunta_19 = RadioField(u'19 - Suponga que desea obtener los mejores resultados en un examen escrito, que va a ser mentalmente muy desgastante y durará 2 horas, pero Ud. puede elegir libremente el horario para hacerlo. ¿Cuál elegiría, pensando en aquel en que le va resultar más fácil responderlo?',
                             choices=[('A', u'8:00 -10:00'),
                                      ('B', u'11:00 - 13:00'),
                                      ('C', u'15:00 - 17:00 '),
                                      ('D', u'19:00 - 21:00')])
    pregunta_20 = RadioField(u'20- Si se fuera a dormir a las 23:00, ¿Qué nivel de cansancio o sueño sentiría?',
                             choices=[('A', u'Nada', ),
                                      ('B', u'Poco'),
                                      ('C', u'Bastante'),
                                      ('D', u'Mucho')])
    pregunta_21 = RadioField(u'21 - Si por alguna razón Ud. se va a dormir algunas horas más tarde de lo habitual, pero al otro día no tiene necesidad de despertarse en el mismo horario de todos los días, ¿Qué le ocurriría?',
                             choices=[('A', u'Se despertaría a la hora habitual y ya no dormiría'),
                                      ('B', u'Se despertaría a la hora habitual y se sentiría somnoliento'),
                                      ('C', u'Se despertaría a la hora habitual y se volvería a dormir inmediatamente'),
                                      ('D', u'Se despertaría más tarde de lo habitual')])
    pregunta_22 = RadioField(u'22 - Si una noche Ud. tiene que quedarse despierto entre las 4 y las 6 de la madrugada para hacer algún tipo de vigilancia, como cuidar a alguien, y al otro día no tiene compromisos, ¿Qué haría?',
                             choices=[('A', u'Se quedaría despierto hasta empezar y recién se iría a dormir después de las 6:00'),
                                      ('B', u'Dormiría un poco (una siesta) antes y recién se iría a dormir “bien” después de las 6:00'),
                                      ('C', u'Dormiría hasta las 4:00 y luego completaría su  sueño con alguna/s hora/s más después de las 6:00.'),
                                      ('D', u'Dormiría “bien” hasta las 4:00 y después de las 6:00 ya no necesitaría hacerlo')])

    pregunta_23 = RadioField(u'23 - Si tuviera que hacer un trabajo que le demanda un esfuerzo físico muy grande durante 2 horas y fuera libre de planificar su día, ¿en qué momento del día lo haría?',
        choices=[(u'A', u'8:00 -10:00'),
                 (u'B', u'11:00 - 13:00'),
                 (u'C', u'15:00 - 17:00'),
                 (u'D', u'19:00 - 21:00')])
    pregunta_24 = RadioField(u'24 - Un amigo lo invita a hacer ejercicio o practicar un deporte entre las 22:00 y las 23:00. Pensando en los horarios en los que Ud. se siente mejor, ¿cómo cree que sería su rendimiento?',
        choices=[(u'A', u'Muy bueno'),
                 (u'B', u'Razonable'),
                 (u'C', u'Pobre'),
                 (u'D', u'Malo')])
    pregunta_25 = FormField(HourFormPregunta18, u'25 - Si Ud. pudiera elegir los horarios de su trabajo, el cual es realmente entretenido y en el cual se le paga de acuerdo a su rendimiento, suponiendo que trabaja 5 horas corridas, ¿qué horario elegiría? ')
    pregunta_26 = FormField(HourFormPregunta18, u'26 - ¿A qué hora del día se siente mejor habitualmente (más fresco, más activo, más despierto, más capaz, etc.)?')
    pregunta_27 = RadioField(u'27 - Si tuviera que definirse como un tipo de persona “matutina (mañanera)” o “vespertina (nocturna)”, ¿Cómo se definiría?',
                             choices=[(u'A', u'Definitivamente mañanera'),
                                      (u'B', u'Más mañanera que vespertina'),
                                      (u'C', u'Más vespertina que mañanera'),
                                      (u'D', u'Definitivamente vespertina')])
