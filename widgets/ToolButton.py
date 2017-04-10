# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# ToolButton
class KiangToolButton(QtWidgets.QToolButton):

    def __init__(self, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 buttonStyle = QtCore.Qt.ToolButtonTextUnderIcon,
                 checkable = True, text = "",
                 icon = False, parent = None):

        QtWidgets.QToolButton.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QToolButton{border: none; background: transparent; color: #ffffff} QToolButton:checked{color:#d82d54}")
        # Set cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        #Button style
        self.setToolButtonStyle(buttonStyle)
        # Checkable
        self.setCheckable(True)
        # Text
        self.setText(text)
        # Icon
        if icon:

            self.setIcon(icon)

    @classmethod
    def menuToolButton(cls, text, icon):

        return cls(text = text, icon = icon)

    @classmethod
    def listToolButton(cls, font, text, icon):

        return cls(font = font, text = text, icon = icon)
        
