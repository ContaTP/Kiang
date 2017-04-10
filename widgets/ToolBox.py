# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# ToolBox
class KiangToolBox(QtWidgets.QToolBox):

    def __init__(self, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.Qt.Bold),
                 backgroundColor = "transparent", fontColor = "#5a5e5a", selectedColor = "#5a5e5a") 

        QtWidgets.QToolBox.__init__(self, parent)
        self.setStyleSheet("QToolBox{border: none;} QToolBox::tab{border: none; background: %s; color: %s;} QToolBox::tab:selected{ border: none; border-bottom: 2px solid %s;}" %(backgroundColor, fontColor, selectedColor))
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)


    def addItem(self, itemList):

        super(KiangToolBox, self).addItem(itemList)
        
