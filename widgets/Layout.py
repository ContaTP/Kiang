# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Layout
# BoxLayout
class KiangBoxLayout(QtWidgets.QBoxLayout):

    def __init__(self, direction = 0,
                 contentsMargins = [0, 0, 0, 0], spacing = 0, parent = None):

        QtWidgets.QBoxLayout.__init__(self, direction, parent)
        # Set contents margins
        left, top, right, bottom = contentsMargins
        self.setContentsMargins(left, top, right, bottom)
        # Set spacing
        self.setSpacing(spacing)

    def addWidget(self, widgetList, stretchList = None):

        if isinstance(widgetList, QtWidgets.QWidget):

            if not stretchList:

                stretchList = 1
                
            super(KiangBoxLayout, self).addWidget(widgetList, stretchList)

        elif isinstance(widgetList, list):

            # If no stretch factor is given, default are equal stretch
            if not stretchList:

                stretchList = [1] * len(widgetList)
                
            for index, widget in enumerate(widgetList):

                super(KiangBoxLayout, self).addWidget(widget, stretchList[index])

        else:

            return

# GridLayout
class KiangGridLayout(QtWidgets.QGridLayout):

    def __init__(self, spacing = 0, parent = None):

        QtWidgets.QGridLayout.__init__(self, parent)
        # Set contents margins
        self.setSpacing(spacing)

    def addWidget(self, widgetList, spanList):

        if isinstance(widgetList, QtWidgets.QWidget):

            if not spanList:

                row, col, rowSpan, colSpan = [1, 1, 1, 1]
                
            else:

                row, col, rowSpan, colSpan = spanList
                
            super(KiangGridLayout, self).addWidget(widgetList, row, col, rowSpan, colSpan)

        elif isinstance(widgetList, list):

            # If no stretch factor is given, default are equal stretch
            if not spanList:

                spanList = [[1, 1, 1, 1]] * len(widgetList)
                
            for index, widget in enumerate(widgetList):
                
                row, col, rowSpan, colSpan = spanList[index]
                super(KiangGridLayout, self).addWidget(widget, row, col, rowSpan, colSpan)

        else:

            return        

        
