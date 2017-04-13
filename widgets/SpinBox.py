"""
Re-implement the QSpinBox in Qt
"""

# PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QSpinBox


class KiangSpinBox(QSpinBox):
    
    def __init__(self, borderColor = "#5a5e5a",
                 cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 min = None, max = None, parent = None):
        
        QSpinBox.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QSpinBox{border: 1px solid %s; border-radius: 5px;} QSpinBox::up-button{border: none;} QSpinBox::down-button{border:none}  QSpinBox::up-arrow{ image: url(./resources/images/uparrow_button.png); width: 10px; height: 10px;} QSpinBox::down-arrow{image: url(./resources/images/downarrow_button.png); width: 10px; height: 10px;}" %borderColor)
        # Cusor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Set minimum and maximum
        if min:
            
            self.setMinimum(min)
            
        if max:
            
            self.setMaximum(max)
            
            