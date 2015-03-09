# -*- coding: utf-8 -*-

from flask import current_app
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError, \
    RadioField, FormField, SelectField, IntegerField, HiddenField, DateField, StringField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo, \
    Optional, NumberRange, Required
from wtforms.widgets.core import Select, HTMLString, html_params
from wtforms.widgets import TextArea


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
        Length(min=6, max=50, message=u'La contraseña tiene que ser de al menos 6 caracteres'),
        EqualTo('confirm', message=u'Las contraseñas deben coincidir.'),
        Regexp(r'[A-Za-z0-9@#$%^&+=]',
               message=u'La contraseña tiene que tener caracteres válidos')
    ],
    'hora': [
        Required(),
        Length(min=4, max=4)
    ],
    'age': [
        NumberRange(min=0, max=100,
                    message=u'Por favor ingresa tu edad entre 0 y 100 años')
    ],
    'edad': [
        Required()
    ]
}


class RegisterForm(Form):
    class Meta:
        locales = ['es_ES', 'es']
    email = TextField('Email', validators['email'])
    password = PasswordField(u'Contraseña', validators['password'], )
    confirm = PasswordField(u'Confirmar contraseña')
    name = TextField('Nombre', validators['edad'])
    twitter_handle = TextField('Twitter (Opcional)')
    # work = SelectField(u'¿Trabajas?',
    #                    choices=[(u'Si', u'Si'), (u'No', u'No')])
    # study = SelectField(u'¿Estudias?',
    #                     choices=[(u'Si', u'Si'), (u'No', u'No')])
    age = IntegerField('Edad', validators['age'])
    sex = SelectField(u'¿Genero?',
                       choices=[(u'female', u'Femenino'), (u'male', u'Masculino'), (u'other', u'Otro')])
    next = HiddenField()


class HourForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(HourForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 24)]
    minute_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices.insert(0, (u'empty', u'--'))
    hour_choices.insert(0, (u'empty', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta9(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(HourFormPregunta9, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(5, 13)]
    minute_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices.insert(0, (u'empty', u'--'))
    hour_choices.insert(0, (u'empty', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta10(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(HourFormPregunta10, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(u'empty', u'--'), (u'20', u'20'), (u'21', u'21'),
                    (u'22', u'22'), (u'23', u'23'), (u'00', u'00'), (u'01', u'01'),
                    (u'02', u'02'), (u'03', u'03')]
    minute_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices.insert(0, (u'empty', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta18(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(HourFormPregunta18, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(u'empty', u'--'), (u'20', u'20'), (u'21', u'21'),
                    (u'22', u'22'), (u'23', u'23'), (u'00', u'00'), (u'01', u'01'),
                    (u'02', u'02'), (u'03', u'03')]
    minute_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices.insert(0, (u'empty', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class NacimientoForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(NacimientoForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']

    mes = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(1, 13)]
    anio = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(1910, 2015)]
    anio.insert(0, (u'empty', u'--'))
    mes.insert(0, (u'empty', u'--'))
    mes_field = SelectField(u'Mes:', choices=mes)
    anio_field = SelectField(u'Año:', choices=anio)


class PorqueElegisteElTurnoForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(PorqueElegisteElTurnoForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']

    choice_field = RadioField(u'Turno en el que cursas ANÁLISIS MATEMÁTICO.',
                             choices=[(u'horario_de_trabajo', u'Por compatibilidad con mi horario de trabajo'),
                                      (u'me_siento_mejor', u'Porque es el horario en el que me siento mejor'),
                                      (u'mas_comodo_otras_actividades', u'Porque me queda más cómodo por mis otras actividades no laborales'),
                                      (u'otros', u'Otros')])
    others_field = TextField(u'Aclaración')


class CronotiposForm(Form):
    class Meta:
        locales = ['es_ES', 'es']

    # mail_up = db.Column(db.String)
    # fecha_nacimiento = db.Column(db.String)
    # genero = db.Column(db.String)
    # turno_analisis = db.Column(db.String)
    # porque_elegiste_turno = = db.Column(db.String)
    # trabajas = db.Column(db.String)

    genero = RadioField(u'Genero (Según tu DNI).', choices=[('Femenino', 'Femenino'),('Masculino', 'Masculino')])
    fecha_nacimiento = FormField(NacimientoForm, label=u'Mes y Año de nacimiento')

    email = TextField(u'Dirección de email de UP', [Required(), Email()])
    turno_analisis = RadioField(u'Turno en el que cursas ANÁLISIS MATEMÁTICO.', choices=[(u'manana', u'Mañana'),('Tarde', 'Tarde'),('Noche', 'Noche')])
    porque_elegiste_turno = FormField(PorqueElegisteElTurnoForm, label=u'¿Por qué elegiste ese turno? *')
    trabajas = RadioField(u'¿Trabajás?', choices=[('Si', 'Si'),('No', 'No')])



    pregunta_1 = FormField(HourForm, label=u'1 - Me acuesto a las ... (Ejemplo 22:00)')

    #pregunta_2 = FormField(HourForm, label=u'2 - Necesito ... minutos para quedarme dormido')
    minute_choices2 = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices2.insert(0, (u'empty', u'--'))

    pregunta_2 = SelectField(u'2 - Tardo ... minutos para quedarme dormido', choices=minute_choices2)


    pregunta_3 = FormField(HourForm, label=u'3 - Me despierto a las ... (Ejemplo 22:00)')

    pregunta_4 = RadioField(u'4 - ¿Cuán bien dormís en los días libres? (Ejemplo: 1 Muy Mala, 10 Excelente)', choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')])

    pregunta_5 = FormField(HourForm, label=u'5 - Me acuesto a las ... (Ejemplo 22:00)')


    #pregunta_6 = FormField(HourForm, label=u'6 - Necesito ... minutos para quedarme dormido (Ejemplo: 05 para 5 minutos)')
    minute_choices6 = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices6.insert(0, (u'empty', u'--'))
    pregunta_6 = SelectField(u'6 - Necesito ... minutos para quedarme dormido (Ejemplo: 05 para 5 minutos)', choices=minute_choices6)

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
                           label=u'9 - Si pudiera planear libremente su día ¿A qué hora se levantaría? (Ejemplo 08:00)', )

    pregunta_10 = FormField(HourFormPregunta10,
                            label=u'10 - Si pudiera planear libremente su día ¿A qué hora se acostaría? (Ejemplo 22:00)')


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
                                      ('D', u'Nada')])

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
    pregunta_25 = FormField(HourForm, u'25 - Si Ud. pudiera elegir los horarios de su trabajo, el cual es realmente entretenido y en el cual se le paga de acuerdo a su rendimiento, suponiendo que trabaja 5 horas corridas, ¿Qué horario elegiría?. POR FAVOR, seleccione LA PRIMERA de las cinco horas corridas.')
    pregunta_26 = FormField(HourForm, u'26 - ¿A qué hora del día se siente mejor habitualmente (más fresco, más activo, más despierto, más capaz, etc.)?')
    pregunta_27 = RadioField(u'27 - Si tuviera que definirse como un tipo de persona “matutina (mañanera)” o “vespertina (nocturna)”, ¿Cómo se definiría?',
                             choices=[(u'A', u'Definitivamente mañanera'),
                                      (u'B', u'Más mañanera que vespertina'),
                                      (u'C', u'Más vespertina que mañanera'),
                                      (u'D', u'Definitivamente vespertina')])
    comments = StringField(u'Comentarios Libres', widget=TextArea())
