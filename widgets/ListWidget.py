# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


class KiangListWidget(QtWidgets.QListWidget):

    def __init__(self, backgroundColor = "#5a5e5a", parent = None):
        
        QtWidgets.QListWidget.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QListWidget{color:%s; padding-right: 20px; padding-left: 20px;} QListView::item{border: none; border-radius: 5px; padding: 10px 15px 10px 5px;} QListView::item:hover{background: #eeeeee;} QListView::item:selected{color: #ffffff; border: 0; outline: 0; background: #2dd8b1;}" %backgroundColor)
        # Cursor
        self.setCursor(QtCore.Qt.PointingHandCursor)
        # Focus
        self.setFocusPolicy(QtCore.Qt.NoFocus)

    def addItem(self, itemList):

        if isinstance(itemList, QtWidgets.QListWidgetItem):
            
            super(KiangListWidget, self).addItem(itemList)

        elif isinstance(itemList, list):

            for widgetItem in itemList:

                super(KiangListWidget, self).addItem(widgetItem)

        else:

            return


class KiangListWidgetItem(QtWidgets.QListWidgetItem):

    def __init__(self, icon, text, font = QtGui.QFont("Glacial Indifference", 20), parent = None):

        QtWidgets.QListWidgetItem.__init__(self, parent)
        # Set icon
        self.setIcon(icon)
        # Set font
        self.setFont(font)
        
    def setIcon(self, icon):

        super(KiangListWidgetItem, self).setIcon(icon)
        
    def setSizeHint(self, size):

        super(KiangListItem, self).setSizeHint(size)
