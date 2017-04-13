"""
Re-implement the QCheckBox in Qt
"""

# PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QCheckBox

# CheckBox
class KiangCheckBox(QCheckBox):
    
    def __init__(self, checked = False, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 text = "", parent = None):
        
        QCheckBox.__init__(self, parent)
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