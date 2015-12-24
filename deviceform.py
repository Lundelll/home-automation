from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from content_manager import Protocols, Models


class DeviceForm(Form):
    models = Models()
    name = StringField('Name', validators=[DataRequired])
    # protocol = StringField('protocol', validators=[DataRequired])
    model = SelectField('Model', choices=models.get('arctech'))
    protocol = SelectField('Protocol', choices=Protocols())

    '''
    core.add_device("test lamp",
                               "arctech",
                               "codeswitch",
                               house=1,
                               unit=1)
    '''
