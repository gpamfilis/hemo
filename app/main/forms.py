from flask_wtf import Form
from wtforms import FloatField, SubmitField, SelectField


class Weight(Form):
    weight = FloatField('Weight')
    ok = SubmitField('Ok')


class BMI(Form):
    weight = FloatField('Weight')
    height = FloatField('Height')
    ok = SubmitField('Ok')

class BathRoom(Form):
    output = SelectField("What Happened There!!!!!?????", choices=[(0,'Poopie'), (1,'Peepie')], coerce=int)
    rate = SelectField("Rate it", choices=[(0,'1'), (1,'2'),(2,'3'),(3,'4'),(4,'5')], coerce=int)
    ok = SubmitField('Confess!!!!!')
