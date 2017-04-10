# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# TextEdit
class KiangTextEdit(QtWidgets.QTextEdit):

    def __init__(self, cursor = QtCore.Qt.IBeamCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 backgroundColor = "#ffffff", fontColor = "#5a5e5a", parent = None):

        QtWidgets.QTextEdit.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QTextEdit{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
