# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

KiangMessagerBackgroundColor = {"ErrorMessager": "#ff4430", "WarningMessager": "yellow", "InfoMessager": "blue", "ProgressMessager": "green"}
KiangMessagerFontColor = {"ErrorMessager": "#ffffff", "WarningMessager": "#ffffff", "InfoMessager": "#ffffff", "ProgressMessager": "#ffffff"}
"""
Messager Class, used to provide error, warning, message information

"""
class KiangMessager(QtWidgets.QLabel):

    def __init__(self, font = QtGui.QFont("Glacial Indifference", 10), parent = None):

        QtWidgets.QLabel.__init__(self, parent)
        # Font
        self.setFont(font)
        # Text
        self.setText("")
        # Hide
        self.hide()

    def message(self, msg, msgType):

        if msgType == "VoidMessager":

            msg = ""
            self.hide()
            return

        # Stylesheet
        self.setStyleSheet("background: %s; border-radius: 5px; padding-left: 10px; color: %s;" %(KiangMessagerBackgroundColor[msgType], KiangMessagerFontColor[msgType]))
        # Text
        self.setText(msg)
        self.show()
        return
        
