# PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel


# Label
class KiangLabel(QLabel):

    def __init__(self, backgroundColor = "transparent", cursor = QtCore.Qt.ArrowCursor, 
                 font = QtGui.QFont("Glacial Indifference", 10), fontColor = "#5a5e5a", 
                 hidden = False, margin = 5, parent = None, text = ""):

        QLabel.__init__(self, text, parent)
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Hidden
        if hidden:
            
            self.setHidden(True)
            
        # Margin
        self.setMargin(margin)
        
