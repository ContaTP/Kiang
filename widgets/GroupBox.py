# PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QGroupBox, QWidget

# ToolBox
class KiangGroupBox(QGroupBox):

    def __init__(self, backgroundColor = "transparent", cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10), fontColor = "#5a5e5a",
                 hidden = False, parent = None): 

        QGroupBox.__init__(self, parent)
        self.setStyleSheet("QGroupBox{border: none; background: %s; color: %s}" %(backgroundColor, fontColor))
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Hide
        if hidden:
            
            self.setHidden(True)


    def addItem(self, itemList):

        if isinstance(itemList, QWidget):
            
            super(KiangGroupBox, self).addItem(itemList)

        elif isinstance(itemList, list):

            for widgetItem in itemList:

                super(KiangGroupBox, self).addItem(widgetItem)

        else:

            return        
