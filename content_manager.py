#! /usr/bin/python3
# -*- coding: utf-8 -*-


def Menu():
    MENU_CHOICES = [["Visa alla enheter", "/devices/"],
                    ["Visa alla grupper", "/groups/"],
                    ["Lägg till ny enhet", "/device/add/"],
                    ["Tänd alla lamporna", "/"]]

    return MENU_CHOICES


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


def Models():
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