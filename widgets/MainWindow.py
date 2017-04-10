# PyQt5
from PyQt5 import QtCore, QtWidgets

# MainWindow
class KiangMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = None):

        QtWidgets.QMainWindow.__init__(self, parent)
        # Background
        self.setStyleSheet("background: #f5f5f5;")
        # Window title
        self.setWindowTitle("KiANG")
        # Size of the window
        self.resize(QtCore.QSize(1200, 800))
        # Minimum size
        self.setMinimumSize(QtCore.QSize(900, 600))
        # Centralwidget
        self.centralWidget = QtWidgets.QWidget()
        # Set central widget
        self.setCentralWidget(self.centralWidget)


    def setCentralWidgetLayout(self, layout):

        self.centralWidget.setLayout(layout)
