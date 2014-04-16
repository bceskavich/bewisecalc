from flask.ext.wtf import Form
from wtforms import IntegerField, SelectField
from wtforms.validators import Required

class BACForm(Form):
    beer = IntegerField('beer', default = 0, id="bac-input")
    wine = IntegerField('wine', default = 0, id="bac-input")
    liqour = IntegerField('liqour', default = 0, id="bac-input")
    hours = IntegerField('hours'    , validators = [Required()], id="info-input")
    weight = IntegerField('weight', validators = [Required()], id="info-input")
    gender = SelectField('gender', choices=[('male', 'Male'), ('female', 'Female')], id="gender")
