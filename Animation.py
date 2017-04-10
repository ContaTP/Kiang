# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

"""
Animation for widget
"""
class TransitionWidget(QtWidgets.QWidget):

    def __init__(self, old_widget, duration, parent = None):

        QtWidgets.QWidget.__init__(self, parent)
        # Resize
        self.resize(parent.size())
        # Transition
        self.old_pixmap = QtGui.QPixmap(parent.size())
        old_widget.render(self.old_pixmap)
        # No opacity when initialized
        self.pixmap_opacity = 1.0
        # Timeline
        self.timeline = QtCore.QTimeLine()
        self.timeline.setDuration(duration)
        # Signal
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)

        # Strat timeline
        self.timeline.start()

    def paintEvent(self, event):
    
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    
    def animate(self, value):
    
        self.pixmap_opacity = 1.0 - value
        self.repaint()
    
