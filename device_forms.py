from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms import widgets
from content_manager import protocols, models, devices, houses, numbers
from custom_widgets import CustomListWidgetRemoveDevice


class CreateDeviceForm(Form):
    name = StringField('Name', validators=[DataRequired])
    model = SelectField('Model', choices=models())
    protocol = SelectField('Protocol', choices=protocols())
    house = SelectField('Houses', choices=houses())
    number = SelectField('Numbers', choices=numbers())


class RemoveDeviceForm(Form):
    dev = []
    if len(devices()) > 0:
        for device in devices():
            dev.append((device.id, device.name))

    widgets.ListWidget()
    device_choices = SelectMultipleField('Devices', choices=dev,
                                         option_widget=widgets.CheckboxInput(),
                                         widget=CustomListWidgetRemoveDevice())
