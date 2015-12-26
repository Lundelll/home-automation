from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from content_manager import Protocols, Models


class DeviceForm(Form):
    name = StringField('Name', validators=[DataRequired])
    # protocol = StringField('protocol', validators=[DataRequired])
    model = SelectField('Model', choices=Models())
    protocol = SelectField('Protocol', choices=Protocols())
