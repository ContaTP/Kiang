# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# ToolBox
class KiangGroupBox(QtWidgets.QGroupBox):

    def __init__(self, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 backgroundColor = "transparent", fontColor = "#5a5e5a"): 

        QtWidgets.QGroupBox.__init__(self, parent)
        self.setStyleSheet("QGroupBox{border: none; background: %s; color: %s}" %(backgroundColor, fontColor))
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)


    def addItem(self, itemList):

        super(KiangGroupBox, self).addItem(itemList)
        
