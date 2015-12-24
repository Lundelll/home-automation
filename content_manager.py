#! /usr/bin/python3
# -*- coding: utf-8 -*-


def Menu():
    MENU_CHOICES = [["Visa alla enheter", "/devices/"],
                    ["Visa alla grupper", "/groups/"],
                    ["Tänd alla lamporna", "/"]]

    return MENU_CHOICES


def Models():
    MODEL_CHOICES = {"arctech": [("", ""),
                                 ("codeswitch", "codeswitch"),
                                 ("selflearning-switch",
                                  "selflearning-switch"),
                                 ("selflearning-dimmer",
                                  "selflearning-dimmer"),
                                 ("bell", "bell")],
                     "brateck": [],
                     "everflourish": [],
                     "fuhaote": [],
                     "hasta": [],
                     "ikea": [],
                     "kangtai": [],
                     "risingsun": [("", ""),
                                   ("codeswitch", "codeswitch"),
                                   ("selflearning", "selflearning")],
                     "sartano": [],
                     "silvanachip": [("", ""),
                                     ("ecosavers", "ecosavers"),
                                     ("kp100", "kp100")],
                     "upm": [],
                     "waveman": [],
                     "x10": []
                     }

    return MODEL_CHOICES


def Protocols():
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
