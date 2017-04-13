# PyQt5
from PyQt5 import QtWidgets

class KiangFrame(QtWidgets.QFrame):

    def __init__(self, backgroundColor = "#f5f5f5", enabled = True,
                 hidden = False, parent = None):

        QtWidgets.QFrame.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QFrame{background: %s; border: none;}" %backgroundColor)
        # Autofill background
        self.setAutoFillBackground(True)
        # Set enabled
        if not enabled:
            
            self.setEnabled(False)
            
        # Set hidden
        if hidden:
            
            self.setHidden(True)
