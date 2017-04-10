# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Splitter
class KiangSplitter(QtWidgets.QSplitter):

    def __init__(self, direction, parent = None):

        QtWidgets.QSplitter.__init__(self, parent)

    def addWidget(self, widgetList):

        super(KiangSplitter, self).addWidget(widgetList)
