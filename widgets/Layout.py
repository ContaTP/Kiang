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

        # If there is only one widget
        if isinstance(widgetList, QtWidgets.QWidget):
            
            # If the span factor is not set, the default start at 0, 0 and span 1, 1
            if not spanList:

                row, col, rowSpan, colSpan = [0, 0, 1, 1]
                
            else:

                row, col, rowSpan, colSpan = spanList
                
            super(KiangGridLayout, self).addWidget(widgetList, row, col, rowSpan, colSpan)
        
        
        # If there are multiple widgets
        elif isinstance(widgetList, list):

            # If no stretch factor is given, default are equal stretch in a row
            if not spanList:

                for col in range(0, len(widgetList)):
                    
                    super(KiangGridLayout, self).addWidget(widget, 0, col, 1, 1)
            
            else:
                    
                for index, widget in enumerate(widgetList):
                
                    row, col, rowSpan, colSpan = spanList[index]
                    super(KiangGridLayout, self).addWidget(widget, row, col, rowSpan, colSpan)

        else:

            return        

        
