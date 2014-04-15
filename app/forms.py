from flask.ext.wtf import Form
from wtforms import IntegerField, SelectField
from wtforms.validators import Required

class BACForm(Form):
    beer = IntegerField('beer', default = 0, id="bac-input")
    wine = IntegerField('wine', default = 0, id="bac-input")
    liqour = IntegerField('liqour', default = 0, id="bac-input")
    hours = IntegerField('hours', default = 0, validators = [Required()], id="bac-input")
    weight = IntegerField('weight', default = 0, validators = [Required()], id="bac-input")
    gender = SelectField('gender', choices=[('male', 'Male'), ('female', 'Female')], id="gender")
