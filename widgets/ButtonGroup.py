# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Button Group
class KiangButtonGroup(QtWidgets.QButtonGroup):

    def __init__(self, exclusived = True, parent = None):

        QtWidgets.QButtonGroup.__init__(self, parent)
        # Set exlcusive
        self.setExclusive(exclusived)

    # Rewrite the add button method to allow add a list
    def addButton(self, buttonList):

        for index, button in enumerate(buttonList):

            super(KiangButtonGroup, self).addButton(button, index)
