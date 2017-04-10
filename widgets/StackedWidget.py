# PyQt5
from PyQt5 import QtCore, QtWidgets
from Animation import TransitionWidget

# StackedWidget
class KiangStackedWidget(QtWidgets.QStackedWidget):

    def __init__(self, parent = None):

        QtWidgets.QStackedWidget.__init__(self, parent)

    def addWidget(self, widgetList):

        if isinstance(widgetList, QtWidgets.QWidget):

             super(KiangStackedWidget, self).addWidget(widgetList)

        elif isinstance(widgetList, list):
            
             for widget in widgetList:

                 super(KiangStackedWidget, self).addWidget(widget)

        else:

            return

    def setStackIndex(self, index, animation = True):

        # If there is animation
        if animation:

            fader_widget = TransitionWidget(self.currentWidget(), 300, self.widget(index))
            del fader_widget
        
        self.setCurrentIndex(index)
