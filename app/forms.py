from flask.ext.wtf import Form
from wtforms import IntegerField, SelectField, FloatField
from wtforms.validators import Required

# Simple BAC form, with appropriate inputs and requirements
class BACForm(Form):
    beer = IntegerField('beer', default = 0, id="bac-input")
    wine = IntegerField('wine', default = 0, id="bac-input")
    liqour = IntegerField('liqour', default = 0, id="bac-input")
    hours = FloatField('hours', validators = [Required()], id="info-input")
    weight = IntegerField('weight', validators = [Required()], id="info-input")
    gender = SelectField('gender', choices=[('male', 'Male'), ('female', 'Female')], id="gender")
