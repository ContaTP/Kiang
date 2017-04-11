"""
Re-write all button widgets in Qt
"""
# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# PushButton
class KiangPushButton(QtWidgets.QPushButton):

    def __init__(self, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 text = "", icon = False,  backgroundColor = "#5a5e5a",
                 backgroundHoverColor = "#ff4430", fontColor = "#ffffff", parent = None):

        QtWidgets.QPushButton.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QPushButton{background: %s; border: none; border-radius: 5px; padding: 10px 20px 10px 20px; margin: 0 30px 0 30px; color: %s;} QPushButton:hover{background: %s;}" %(backgroundColor, fontColor, backgroundHoverColor))
        # Set cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Text
        self.setText(text)
        # Icon
        if icon:

            self.setIcon(icon)


# RadioButton
class KiangRadioButton(QtWidgets.QRadioButton):
    
    def __init__(self, checked = False, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 text = "", parent = None):
        
        QtWidgets.QRadioButton.__init__(self, parent)
        # Stylesheet
        # No stylesheet yet 
        # Cusor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Text
        self.setText(text)
        # Checked
        self.setChecked(checked)
        # Icon
        if icon:
            
            self.setIcon(icon)


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
        
