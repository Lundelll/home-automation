#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect, request
import tellcore.telldus as td
import tellcore.constants as const
from content_manager import Menu
from deviceform import DeviceForm


MENU_CHOICES = Menu()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', MENU_CHOICES=MENU_CHOICES)


@app.route('/devices/')
def devices():
    devices_menu = []
    for device in get_devices():
        if device.type == const.TELLSTICK_TYPE_DEVICE:
            devices_menu.append(
                [device.name, "/device/" + str(device.id) + "/"])

    return render_template('index.html', MENU_CHOICES=devices_menu)


@app.route('/device/<id>/')
def device(id):
    device = td.DeviceFactory(int(id))
    return render_template('device.html', device=device)


@app.route('/device/add/', methods=['GET', 'POST'])
def add_device():
    form = DeviceForm(csrf_enabled=False)
    if request.method == 'GET':
        '''
        core = td.TelldusCore()
        lamp = core.add_device("test lamp",
                               "arctech",
                               "codeswitch",
                               house=1,
                               unit=1)

        return "Replace this method to show the form."
        '''
        return render_template('add.html', form=form)

    if request.method == 'POST':
        core = td.TelldusCore()
        lamp = core.add_device(form.name.data, form.protocol.data, form.model.data)
        print(lamp)
        return redirect('/')


@app.route('/device/<id>/remove/')
def remove_device(id):
    try:
        device = td.DeviceFactory(int(id))
        name = device.name
        device.remove()
        return name + " is removed."
    except td.TelldusError:
        return "Error! Are you sure this device exists?"


@app.route('/device/<id>/on/')
def turn_on_device(id):
    try:
        device = td.DeviceFactory(int(id))
        device.turn_on()
        return redirect(url_for('device', id=id))
    except td.TelldusError:
        return "Fail, are you sure the a divice with that ID exists?"


@app.route('/device/<id>/off/')
def turn_off_device(id):
    try:
        device = td.DeviceFactory(int(id))
        device.turn_off()
        return redirect(url_for('device', id=id))
    except td.TelldusError:
        return "Fail, are you sure the a divice with that ID exists?"


@app.route('/groups/')
def rooms():
    try:
        groups = []
        for device in get_devices():
            if device.type == const.TELLSTICK_TYPE_GROUP:
                groups.append([device.name, "/group/" + str(device.id) + "/"])
        return render_template('index.html', MENU_CHOICES=groups)
    except td.TelldusError:
        return "No groups exists"


@app.route('/group/add/<name>/')
def add_room(name):
    try:
        core = td.TelldusCore()
        device = core.add_group(name, None)
        return ("Group " + device.id + ": " +
                device.name + ": " + "has been created")
    except td.TelldusError:
        return "Something went wrong"


@app.route('/group/<id>/')
def get_group(id):
    try:
        device_group = td.DeviceFactory(id)
        devices = device_group.devices_in_group()
        return render_template('devices.html', devices=devices)
    except td.TelldusError:
        return "Something went wrong"


def get_devices():
    core = td.TelldusCore()
    return core.devices()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
