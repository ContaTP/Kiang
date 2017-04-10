# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


# Label
class KiangLabel(QtWidgets.QLabel):

    def __init__(self, cursor = QtCore.Qt.ArrowCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 backgroundColor = "transparent", fontColor = "#5a5e5a",
                 margin = 5, text = "", parent = None):

        QtWidget.QLabel.__init__(self, text, parent)
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Margin
        self.setMargin(margin)
        
