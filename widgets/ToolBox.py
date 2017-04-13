# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# ToolBox
class KiangToolBox(QtWidgets.QToolBox):

    def __init__(self, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 backgroundColor = "transparent", fontColor = "#5a5e5a", 
                 selectedColor = "#5a5e5a", parent = None):

        QtWidgets.QToolBox.__init__(self, parent)
        self.setStyleSheet("QToolBox{border: none;} QToolBox::tab{border: none; background: %s; color: %s;} QToolBox::tab:selected{ border: none; border-bottom: 2px solid %s;}" %(backgroundColor, fontColor, selectedColor))
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)

    # Add item to toolBox
    def addItem(self, itemList, iconList = None, textList = None):

        # If there is one item
        if isinstance(itemList, QtWidgets.QWidget):
            
            # If text is none, default ""
            if textList == None:
                
                textList = ""
                
            super(KiangToolBox, self).addItem(itemList, iconList, textList)

        elif isinstance(itemList, list):

            if iconList == None:
                
                iconList = [None] * len(itemList)
                
            if textList == None:
                
                textList = [""] * len(itemList)
                
            for index, widgetItem in enumerate(itemList):
                
                super(KiangGroupBox, self).addItem(widgetItem, iconList[index], textList[index])

        else:

            return        
        super(KiangToolBox, self).addItem(itemList)
        
