from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms import widgets
from content_manager import protocols, models, devices


class CreateDeviceForm(Form):
    name = StringField('Name', validators=[DataRequired])
    # protocol = StringField('protocol', validators=[DataRequired])
    model = SelectField('Model', choices=models())
    protocol = SelectField('Protocol', choices=protocols())


class RemoveDeviceForm(Form):
    dev = []
    for device in devices():
        dev.append((device.id, device.name))

    device_choices = SelectMultipleField('Devices', choices=dev,
                                         option_widget=widgets.CheckboxInput(),
                                         widget=widgets.ListWidget(
                                             prefix_label=False))
