# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# PushButton
class KiangPushButton(QtWidgets.QPushButton):

    def __init__(self, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 text = "", icon = False,  backgroundColor = "#5a5e5a",
                 backgroundHoverColor = "#ff4430", fontColor = "#ffffff", parent = None):

        QtWidgets.QPushButton.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QPushButton{background: %s; border: none; border-radius: 5px; padding: 10px 20px 10px 20px; margin: 0 30px 0 30px; color: %s;} QPushButton:hover{background: %s;}" %(backgroundColor, fontColor, backgroundHoverColor))
        # Set cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Text
        self.setText(text)
        # Icon
        if icon:

            self.setIcon(icon)
