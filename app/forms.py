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
    minute_choices = [(unicode('%02d' % (x * 5)), unicode('%02d' % (x * 5))) for x in range(0, 12)]
    minute_choices.insert(0, (u'', u'--'))
    hour_choices.insert(0, (u'', u'--'))
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
    minute_choices.insert(0, (u'', u'--'))
    hour_choices.insert(0, (u'', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class MeAcuestoALasForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(MeAcuestoALasForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(19, 24)] + [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 19)]
    minute_choices = [(unicode('%02d' % (x * 5)), unicode('%02d' % (x * 5))) for x in range(0, 12)]
    minute_choices.insert(0, (u'', u'--'))
    hour_choices.insert(0, (u'', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class MeDespiertoALasForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(MeDespiertoALasForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(04, 24)] + [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(00, 04)]
    minute_choices = [(unicode('%02d' % (x * 5)), unicode('%02d' % (x * 5))) for x in range(0, 12)]
    minute_choices.insert(0, (u'', u'--'))
    hour_choices.insert(0, (u'', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta10(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(HourFormPregunta10, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(u'', u'--'), (u'20', u'20'), (u'21', u'21'),
                    (u'22', u'22'), (u'23', u'23'), (u'00', u'00'), (u'01', u'01'),
                    (u'02', u'02'), (u'03', u'03')]
    minute_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices.insert(0, (u'', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class HourFormPregunta18(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(HourFormPregunta18, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']
    hour_choices = [(u'', u'--'), (u'20', u'20'), (u'21', u'21'),
                    (u'22', u'22'), (u'23', u'23'), (u'00', u'00'), (u'01', u'01'),
                    (u'02', u'02'), (u'03', u'03')]
    minute_choices = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(0, 60)]
    minute_choices.insert(0, (u'', u'--'))
    hours_field = SelectField(u'Horas:', choices=hour_choices)
    minutes_field = SelectField(u'Minutos:', choices=minute_choices)


class NacimientoForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(NacimientoForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']

    mes = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(1, 13)]
    anio = [(unicode('%02d' % x), unicode('%02d' % x)) for x in range(1910, 2000)]
    anio.insert(0, (u'', u'--'))
    mes.insert(0, (u'', u'--'))
    mes_field = SelectField(u'Mes:', choices=mes)
    anio_field = SelectField(u'Año:', choices=anio)


class PorqueElegisteElTurnoForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(PorqueElegisteElTurnoForm, self).__init__(*args, **kwargs)

    class Meta:
        locales = ['es_ES', 'es']

    choice_field = RadioField(u'Turno en el que cursas ANÁLISIS MATEMÁTICO.',
                             choices=[(u'horario_de_trabajo', u'Por compatibilidad con mi horario de trabajo.'),
                                      (u'me_siento_mejor', u'Porque es el horario en el que me siento mejor.'),
                                      (u'mas_comodo_otras_actividades', u'Porque me queda más cómodo por mis otras actividades no laborales.'),
                                      (u'otros', u'Otros')])
    others_field = TextField(u'')


class CronotiposForm(Form):
    class Meta:
        locales = ['es_ES', 'es']

    # mail_up = db.Column(db.String)
    # fecha_nacimiento = db.Column(db.String)
    # genero = db.Column(db.String)
    # turno_analisis = db.Column(db.String)
    # porque_elegiste_turno = = db.Column(db.String)
    # trabajas = db.Column(db.String)

    genero = RadioField(u'Género (según tu DNI)', choices=[('Femenino', 'Femenino'),('Masculino', 'Masculino')])
    fecha_nacimiento = FormField(NacimientoForm, label=u'Mes y año de nacimiento')

    email = TextField(u'Dirección de email de UP', [Required()])
    turno_analisis = RadioField(u'Turno en el que cursás ANÁLISIS MATEMÁTICO', choices=[(u'manana', u'Mañana'),('Tarde', 'Tarde'),('Noche', 'Noche')])
    porque_elegiste_turno = FormField(PorqueElegisteElTurnoForm, label=u'¿Por qué elegiste ese turno?')
    trabajas = RadioField(u'¿Trabajás?', choices=[('Si', 'Si'),('No', 'No')])



    pregunta_1 = FormField(MeAcuestoALasForm, label=u'Me acuesto a las ... (Ejemplo 22:10)')

    minute_choices2 = [('00', '00'),
                       ('02', '02'),
                       ('05', '05'),
                       ('10', '10'),
                       ('15', '15'),
                       ('20', '20'),
                       ('30', '30'),
                       ('45', '45'),
                       ('60', '60'),
                       ('90', '90'),
                       ('120', '120')]
    minute_choices2.insert(0, (u'', u'--'))

    pregunta_2 = SelectField(u'Tardo ... minutos para quedarme dormido (Ejemplo: 05 para 5 minutos)', choices=minute_choices2)


    pregunta_3 = FormField(MeDespiertoALasForm, label=u'Me despierto a las ... (Ejemplo 08:05)')

    pregunta_4 = RadioField(u'¿Cuán bien dormís en los días hábiles?', choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')])

    pregunta_duermo_siesta_dia_habil = RadioField(u'En tus días hábiles, ¿dormís siesta cuando podés?', choices=[(u'Sí', u'Sí'),('No', 'No')])

    pregunta_cuanto_duermo_siesta_dia_habil = RadioField(u'Si dormís, ¿cuánto tiempo dormís siesta?',
                    choices=[(u'no_duermo', u'No duermo siesta.'),
                             ('5_a_30', 'de 5 a 30 minutos.'),
                             ('31_a_60', 'de 31 a 60 minutos.'),
                             ('61_a_90', 'de 61 a 90 minutos.'),
                             ('91_a_120', 'de 91 a 120 minutos.')
                             ])


    pregunta_5 = FormField(MeAcuestoALasForm, label=u'Me acuesto a las ... (Ejemplo 22:00)')


    pregunta_6 = SelectField(u'Necesito ... minutos para quedarme dormido (Ejemplo: 05 para 5 minutos)', choices=minute_choices2)

    pregunta_7 = FormField(MeDespiertoALasForm, label=u'Me despierto a las ... (Ejemplo 08:00)')

    pregunta_8 = RadioField(u'¿Cuán bien dormís en los días libres?',
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

    pregunta_duermo_siesta_dia_libre = RadioField(u'En tus días libres, ¿dormís siesta cuando podés?', choices=[(u'Sí', u'Sí'),('No', 'No')])

    pregunta_cuanto_duermo_siesta_dia_libre = RadioField(u'Si dormís, ¿cuánto tiempo dormís siesta?',
                    choices=[(u'no_duermo', u'No duermo siesta.'),
                             ('5_a_30', 'de 5 a 30 minutos.'),
                             ('31_a_60', 'de 31 a 60 minutos.'),
                             ('61_a_90', 'de 61 a 90 minutos.'),
                             ('91_a_120', 'de 91 a 120 minutos.')
                             ])

    pregunta_9 = FormField(MeDespiertoALasForm,
                           label=u'Si pudieras planear libremente tu día, ¿a qué hora te <b>levantarías</b>? (Ejemplo 07:30)', )

    pregunta_10 = FormField(MeAcuestoALasForm,
                            label=u'Si pudieras planear libremente tu día, ¿a qué hora te <b>acostarías</b>? (Ejemplo 21:50)')


    pregunta_11 = RadioField(u'Si tenés que levantarte a una hora específica en la mañana, ¿cuánto dependés de un reloj despertador?', choices=[('A', u'Nada'),('B', u'Poco'),('C', u'Bastante'),('D', u'Mucho')])

    pregunta_12 = RadioField(u'En un día con clima agradable, ¿qué tan fácil te resulta levantarte en la mañana?',
                             choices=[('A', u'Nada fácil'),
                                      ('B', u'No muy fácil'),
                                      ('C', u'Bastante fácil'),
                                      ('D', u'Muy fácil')])

    pregunta_13 = RadioField(u'¿Qué tan atento y despejado te sentís durante la primera media hora después de despertarte en la mañana?',
                             choices=[('A', u'Nada despejado'),
                                      ('B', u'Poco despejado'),
                                      ('C', u'Bastante despejado'),
                                      ('D', u'Muy despejado')])

    pregunta_14 = RadioField(u'¿Qué tanto hambre sentís durante la primera media hora después de despertarte en la mañana?',
                             choices=[('A', u'Nada'),
                                      ('B', u'Poco'),
                                      ('C', u'Bastante'),
                                      ('D', u'Mucho')])
    pregunta_15 = RadioField(u'¿Cuánto cansancio sentís durante la primera media hora después de despertarte en la mañana?',
                             choices=[('A', u'Mucho'),
                                      ('B', u'Bastante'),
                                      ('C', u'Poco'),
                                      ('D', u'Nada')])

    pregunta_16 = RadioField(u'Cuando no tenés nada que hacer al día siguiente, ¿a qué hora te acostás en comparación con lo que acostumbrás?',
                             choices=[('A', u'A la misma hora'),
                                      ('B', u'Menos de 1 hora más tarde'),
                                      ('C', u'Entre 1 y 2 horas más tarde'),
                                      ('D', u'Más de 2 horas más tarde')])
    pregunta_17 = RadioField(u'Un amigo te invita a hacer ejercicio o practicar un deporte entre las 7 y las 8 de la mañana. ¿Cómo crees que será tu rendimiento?',
                             choices=[('A', u'Muy bueno'),
                                      ('B', u'Razonable'),
                                      ('C', u'Pobre'),
                                      ('D', u'Malo')])

    pregunta_18 = FormField(MeAcuestoALasForm,
                           label=u'¿A qué hora de la noche te sentís tan cansado como para irte a dormir? (Ejemplo: 23:15)')

    pregunta_19 = RadioField(u'Suponé que deseás obtener los mejores resultados en un examen escrito, que va a ser mentalmente muy desgastante y durará 2 horas. ¿A qué hora creés que te va a resultar más facil responderlo?',
                             choices=[('A', u'08:00 a 10:00'),
                                      ('B', u'11:00 a 13:00'),
                                      ('C', u'15:00 a 17:00 '),
                                      ('D', u'19:00 a 21:00')])
    pregunta_20 = RadioField(u'Si te fueras a dormir a las 23:00, ¿qué nivel de cansancio o sueño sentirías?',
                             choices=[('A', u'Nada', ),
                                      ('B', u'Poco'),
                                      ('C', u'Bastante'),
                                      ('D', u'Mucho')])
    pregunta_21 = RadioField(u'Si un dia te vas a dormir algunas horas más tarde de lo habitual, pero al otro día no tenés necesidad de despertarte en el mismo horario de todos los días, ¿qué te pasaría?',
                             choices=[('A', u'Me despertaría a la hora habitual y ya no dormiría.'),
                                      ('B', u'Me despertaría a la hora habitual y me sentiría somnoliento.'),
                                      ('C', u'Me despertaría a la hora habitual y me volvería a dormir inmediatamente.'),
                                      ('D', u'Me despertaría más tarde de lo habitual.')])
    pregunta_22 = RadioField(u'Si una noche tenés que quedarte despierto entre las 4 y las 6 de la madrugada para hacer algún tipo de vigilancia, como cuidar a alguien, y al otro día no tenés compromisos, ¿qué harías?',
                             choices=[('A', u'Me quedaría despierto hasta las 4 y me iría a dormir después de las 6.'),
                                      ('B', u'Dormiría un ratito antes y recién me iría a dormir “bien” después de las 6.'),
                                      ('C', u'Dormiría hasta las 4 y luego completaría el sueño con alguna/s hora/s más después de las 6.'),
                                      ('D', u'Dormiría “bien” hasta las 4 y después de las 6 ya no necesitaría dormir.')])

    pregunta_23 = RadioField(u'Si tuvieras que hacer un trabajo que te demanda un esfuerzo físico muy grande durante 2 horas, ¿en qué momento del día elegirías hacerlo?',
        choices=[(u'A', u'08:00 a 10:00'),
                 (u'B', u'11:00 a 13:00'),
                 (u'C', u'15:00 a 17:00'),
                 (u'D', u'19:00 a 21:00')])
    pregunta_24 = RadioField(u'Un amigo te invita a hacer ejercicio o practicar un deporte entre las 22 y las 23 horas. ¿Cómo creés que será tu rendimiento?',
        choices=[(u'A', u'Muy bueno'),
                 (u'B', u'Razonable'),
                 (u'C', u'Pobre'),
                 (u'D', u'Malo')])
    pregunta_25 = FormField(HourForm, u'Imaginá que tenés un trabajo realmente entretenido por el cual se te paga de acuerdo a tu rendimiento. Suponiendo que trabajás 5 HORAS CORRIDAS, si pudieras elegir los horarios de tu trabajo, ¿a qué hora elegirías EMPEZAR? (Ejemplo: 15:45)')
    pregunta_26 = FormField(HourForm, u'¿A qué hora del día te sentís mejor habitualmente (más fresco, más activo, más despierto, más capaz, etc.)? (Ejemplo: 22:15)')
    pregunta_27 = RadioField(u'Si tuvieras que definirte como un tipo de persona “matutina (mañanera)” o “vespertina (nocturna)”, ¿cómo te definirías?',
                             choices=[(u'A', u'Definitivamente mañanera'),
                                      (u'B', u'Más mañanera que vespertina'),
                                      (u'C', u'Más vespertina que mañanera'),
                                      (u'D', u'Definitivamente vespertina')])
    comments = StringField(u'Comentarios Libres', widget=TextArea())
