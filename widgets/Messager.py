# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from .Widgets import KiangLabel

KiangMessagerBackgroundColor = {"ErrorMessager": "#ff4430", "WarningMessager": "yellow",
                                 "InfoMessager": "blue", "ProgressMessager": "green"}
KiangMessagerFontColor = {"ErrorMessager": "#ffffff", "WarningMessager": "#ffffff", 
                          "InfoMessager": "#ffffff", "ProgressMessager": "#ffffff"}


"""
Messager class, used to provide error, warning, message information
"""
class KiangMessager(KiangLabel):

    def __init__(self, font = QtGui.QFont("Glacial Indifference", 10), parent = None):

        super(KiangMessager, self).__init__(font = font, hidden = True, text = "")
        
    # Send message
    def msg(self, msg, msgType):

        if msgType == "VoidMessager":

            msg = ""
            self.hide()
            return

        # Stylesheet
        self.setStyleSheet("""background: %s; border-radius: 5px; padding-left: 10px; 
                           color: %s;""" \
                            %(KiangMessagerBackgroundColor[msgType], KiangMessagerFontColor[msgType]))
        # Text
        self.setText(msg)
        self.show()
        
