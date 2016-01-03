#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect, request
import tellcore.telldus as td
import tellcore.constants as const
import content_manager as cm
from device_forms import CreateDeviceForm, RemoveDeviceForm


MENU_CHOICES = cm.menu()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           MENU_CHOICES=MENU_CHOICES)


@app.route('/devices/')
def devices():
    devices_menu = []

    for device in cm.devices():
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
    form = CreateDeviceForm(csrf_enabled=False)
    if request.method == 'GET':
        return render_template('add.html', form=form)

    if request.method == 'POST':
        core = td.TelldusCore()
        parameters = {'house': form.house.data,
                      'unit': str(form.number.data)}
        lamp = core.add_device(form.name.data,
                               form.protocol.data,
                               form.model.data, **parameters)
        print("Added device: " + str(lamp.id) + " - " + lamp.name)
        print("Form entry name: " + form.name.data +
              "\nprotocol: " + form.protocol.data +
              "\nmodel: " + form.model.data)
        return redirect('/')


@app.route('/device/remove/', methods=['GET', 'POST'])
def remove_device():
    form = RemoveDeviceForm(csrf_enabled=False)
    if request.method == 'GET':
        return render_template('remove.html', form=form)

    if request.method == 'POST':
        if form.device_choices.data is not None or len(form.device_choices.data) > 0:
            for device_id in form.device_choices.data:
                device = td.DeviceFactory(int(device_id))
                print(
                    "Removed device: " + str(device.id) + " - " + device.name)
                device.remove()

        return redirect('/')


@app.route('/device/<id>/on/')
def turn_on_device(id):
    try:
        device = td.DeviceFactory(int(id))
        device.turn_on()
        return redirect(url_for('device', id=id))
    except td.TelldusError:
        return "Fail, are you sure the a device with that ID exists?"


@app.route('/device/<id>/off/')
def turn_off_device(id):
    try:
        device = td.DeviceFactory(int(id))
        device.turn_off()
        return redirect(url_for('device', id=id))
    except td.TelldusError:
        return "Fail, are you sure the a device with that ID exists?"


@app.route('/turnoffeverything/')
def turn_off_everything():
    for device in cm.devices():
        device.turn_off()

    return redirect('/')


@app.route('/groups/')
def rooms():
    try:
        groups = []

        for device in cm.groups():
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
