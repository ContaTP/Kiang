# PyQt5
from PyQt5 import QtWidgets

class KiangFrame(QtWidgets.QFrame):

    def __init__(self, backgroundColor = "#f5f5f5", parent = None):

        QtWidgets.QFrame.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QFrame{background: %s; border: none;}" %backgroundColor)
        # Autofill background
        self.setAutoFillBackground(True)
