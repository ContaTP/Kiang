# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Line edit
class KiangLineEdit(QtWidgets.QLineEdit):

    def __init__(self, backgroundColor = "#ffffff", cursor = QtCore.Qt.IBeamCursor,
                 font = QtGui.QFont("Glacial Indifference", 10), fontColor = "#5a5e5a",
                 maxLength = 20, parent = None):

        QtWidgets.QLineEdit.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QLineEdit{background: %s; border: 1px solid #5a5e5a; border-radius: 5px; color: %s}" %(backgroundColor, fontColor))
        # Font
        self.setFont(font)
        # Max length
        self.setMaxLength(maxLength)


