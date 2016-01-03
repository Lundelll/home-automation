#! /usr/bin/python3
# -*- coding: utf-8 -*-
import tellcore.telldus as td
import tellcore.constants as const


def menu():
    MENU_CHOICES = [["Visa alla enheter", "/devices/"],
                    ["Visa alla grupper", "/groups/"],
                    ["Lägg till ny enhet", "/device/add/"],
                    ["Ta bort en enhet", "/device/remove/"],
                    ["Släck alla lamporna", "/turnoffeverything/"]]

    return MENU_CHOICES


def protocols():
    PROTOCOLS = [("", ""),
                 ("arctech", "arctech"),
                 ("brateck", "brateck"),
                 ("hasta", "hasta"),
                 ("ikea", "ikea"),
                 ("kangtai", "kangtai"),
                 ("risingsun", "risingsun"),
                 ("sartano", "sartano"),
                 ("silvanachip", "silvanachip"),
                 ("upm", "upm"),
                 ("waveman", "waveman"),
                 ("x10", "x10")]

    return PROTOCOLS


def models():
    MODEL_CHOICES = [("", ""),
                     ("codeswitch", "codeswitch (arctech)"),
                     ("selflearning-switch (arctech)",
                      "selflearning-switch (arctech)"),
                     ("selflearning-dimmer (arctech)",
                      "selflearning-dimmer (arctech)"),
                     ("bell", "bell (arctech)"),
                     ("selflearning", "selflearning (risingsun)"),
                     ("ecosavers", "ecosavers (silvanachip)"),
                     ("kp100", "kp100 (silvanachip)")]

    return MODEL_CHOICES


def devices():
    core = td.TelldusCore()
    all_devices = []
    for device in core.devices():
        if device.type == const.TELLSTICK_TYPE_DEVICE:
            all_devices.append(device)
    return all_devices


def groups():
    core = td.TelldusCore()
    groups = []
    for device in core.devices():
        if device.type == const.TELLSTICK_TYPE_GROUP:
            groups.append(device)
    return groups
