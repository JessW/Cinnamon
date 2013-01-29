#!/usr/bin/env python

import os
from SettingsWidgets import *
import capi

class Module:
    def __init__(self, content_box):
        keywords = _("screensaver, brightness, lock, password, away, message")
        sidePage = SidePage(_("Screensaver & Brightness"), "screensaver.svg", keywords, content_box)
        self.sidePage = sidePage
        self.name = "screensaver"
        self.category = "prefs"
        if os.path.exists("/usr/bin/cinnamon-screensaver-command"):
            sidePage.add_widget(GSettingsCheckButton(_("Ask for an away message when locking the screen from the menu"), "org.cinnamon.screensaver", "ask-for-away-message", None))
            sidePage.add_widget(GSettingsEntry(_("Default message"), "org.cinnamon.screensaver", "default-message", None))

        widget = capi.get_c_widget("screen")
        if widget is not None:
            self.sidePage.add_widget(widget)
