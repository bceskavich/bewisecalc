from flask.ext.wtf import Form
from wtforms import IntegerField, SelectField
from wtforms.validators import Required

class BACForm(Form):
    beer = IntegerField('beer', default = 0)
    wine = IntegerField('wine', default = 0)
    liqour = IntegerField('liqour', default = 0)
    hours = IntegerField('hours', default = 0, validators = [Required()])
    weight = IntegerField('weight', default = 0)
    gender = SelectField('gender', choices=[('male', 'M'), ('female', 'F')])
