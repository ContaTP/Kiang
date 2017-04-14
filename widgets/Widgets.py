"""
Re-implement widgets in Qt
"""
# PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QPushButton, 
                             QRadioButton, 
                             QToolButton, 
                             QButtonGroup, 
                             QCheckBox, 
                             QFrame, 
                             QGroupBox, 
                             QBoxLayout, 
                             QGridLayout, 
                             QLabel, 
                             QLineEdit, 
                             QListWidget, 
                             QListWidgetItem, 
                             QMainWindow, 
                             QSizePolicy,
                             QSplitter,
                             QSpinBox, 
                             QStackedWidget, 
                             QTextEdit, 
                             QToolBox, 
                             QWidget)

from .Animation import TransitionWidget


"""
PushButton
"""
# PushButton
class KiangPushButton(QPushButton):

    def __init__(self, backgroundColor = "#5a5e5a", backgroundHoverColor = "#ff4430", 
                 cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 fontColor = "#ffffff", text = "", icon = False, parent = None):

        QPushButton.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("""QPushButton{background: %s; border: none; border-radius: 5px; 
                           padding: 10px 20px 10px 20px; margin: 0 30px 0 30px; color: %s;} 
                           QPushButton:hover{background: %s;}""" \
                           %(backgroundColor, fontColor, backgroundHoverColor))
        # Set cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Icon
        if icon:

            self.setIcon(icon)
        # Text
        self.setText(text)



"""
RadioButton
"""
# RadioButton
class KiangRadioButton(QRadioButton):
    
    def __init__(self, backgroundColor = "transparent", 
                 checked = False, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 text = "", parent = None):
        
        QRadioButton.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QRadioButton{background: %s}" %backgroundColor)
        # Cusor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Text
        self.setText(text)
        # Checked
        self.setChecked(checked)


"""
ToolButton
"""
# ToolButton
class KiangToolButton(QToolButton):

    def __init__(self, backgroundColor = "transparent", 
                 buttonStyle = QtCore.Qt.ToolButtonTextUnderIcon,
                 checkable = True, checkedColor = "#f98866", text = "", 
                 cursor = QtCore.Qt.PointingHandCursor, 
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 fontColor = "#ffffff",
                 icon = False, parent = None):

        QToolButton.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("""QToolButton{border: none; background: %s; color: %s} 
                           QToolButton:checked{color:%s}"""% (backgroundColor, fontColor, 
                                                              checkedColor))
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
        


"""
ButtonGroup
"""
# Button Group
class KiangButtonGroup(QButtonGroup):

    def __init__(self, exclusived = True, parent = None):

        QButtonGroup.__init__(self, parent)
        # Set exclusive
        self.setExclusive(exclusived)

    # Rewrite the add button method to allow add a list
    def addButton(self, buttonList):

        for index, button in enumerate(buttonList):

            super(KiangButtonGroup, self).addButton(button, index)



"""
CheckBox
"""
# CheckBox
class KiangCheckBox(QCheckBox):
    
    def __init__(self, backgroundColor = "transparent", 
                 checked = False, cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 text = "", parent = None):
        
        QCheckBox.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QCheckBox{background: %s}" %backgroundColor)
        # Cusor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Text
        self.setText(text)
        # Checked
        if checked:
            
            self.setChecked(True)

        
        
"""
Frame
"""
class KiangFrame(QFrame):

    def __init__(self, backgroundColor = "transparent", enabled = True,
                 hidden = False, parent = None):

        QFrame.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QFrame{background: %s; border: none;}" %backgroundColor)
        # Autofill background
        self.setAutoFillBackground(True)
        # Set enabled
        if not enabled:
            
            self.setEnabled(False)
            
        # Set hidden
        if hidden:
            
            self.setHidden(True)



"""
GroupBox
"""
class KiangGroupBox(QGroupBox):

    def __init__(self, backgroundColor = "transparent", 
                 cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10), 
                 fontColor = "#5a5e5a",
                 hidden = False, title = "", parent = None): 

        QGroupBox.__init__(self, title, parent)
        self.setStyleSheet("QGroupBox{border: none; background: %s; color: %s}" \
                           %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Hide
        if hidden:
            
            self.setHidden(True)


    def addItem(self, itemList):

        if isinstance(itemList, QWidget):
            
            super(KiangGroupBox, self).addItem(itemList)

        elif isinstance(itemList, list):

            for widgetItem in itemList:

                super(KiangGroupBox, self).addItem(widgetItem)

        else:

            return        
        
        
        
"""
Label
"""
# Label
class KiangLabel(QLabel):

    def __init__(self, backgroundColor = "transparent", cursor = QtCore.Qt.ArrowCursor, 
                 font = QtGui.QFont("Glacial Indifference", 10), fontColor = "#5a5e5a", 
                 hidden = False, margin = 5, text = "", parent = None):

        QLabel.__init__(self, text, parent)
        # Stylesheet
        self.setStyleSheet("QLabel{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Hidden
        if hidden:
            
            self.setHidden(True)
            
        # Margin
        self.setMargin(margin)
        
        

"""
BoxLayout
"""
class KiangBoxLayout(QBoxLayout):

    def __init__(self, direction = 0, margins = [0, 0, 0, 0], 
                 spacing = 0, parent = None):

        QBoxLayout.__init__(self, direction, parent)
        # Set contents margins
        left, top, right, bottom = margins
        self.setContentsMargins(left, top, right, bottom)
        # Set spacing
        self.setSpacing(spacing)

    def addWidgetList(self, widgetList, stretchList = None):

        if isinstance(widgetList, QWidget):

            if not stretchList:

                stretchList = 1
                
            self.addWidget(widgetList, stretchList)
            
        elif isinstance(widgetList, list):

            # If no stretch factor is given, default are equal stretch
            if not stretchList:

                stretchList = [1] * len(widgetList)
                
            for index, widget in enumerate(widgetList):

                self.addWidget(widget, stretchList[index])

        else:

            return


"""
GridLayout
"""
# GridLayout
class KiangGridLayout(QGridLayout):

    def __init__(self, spacing = 0, parent = None):

        QGridLayout.__init__(self, parent)
        # Set contents margins
        self.setSpacing(spacing)

    def addWidgetList(self, widgetList, spanList):

        # If there is only one widget
        if isinstance(widgetList, QWidget):
            
            # If the span factor is not set, the default start at 0, 0 and span 1, 1
            if not spanList:

                row, col, rowSpan, colSpan = [0, 0, 1, 1]
                
            else:

                row, col, rowSpan, colSpan = spanList
                
            self.addWidget(widgetList, row, col, rowSpan, colSpan)
        
        
        # If there are multiple widgets
        elif isinstance(widgetList, list):

            # If no stretch factor is given, default are equal stretch in a row
            if not spanList:

                for col in range(0, len(widgetList)):
                    
                    self.addWidget(widget, 0, col, 1, 1)
            
            else:
                    
                for index, widget in enumerate(widgetList):
                
                    row, col, rowSpan, colSpan = spanList[index]
                    self.addWidget(widget, row, col, rowSpan, colSpan)

        else:

            return        



"""
LineEdit
"""
class KiangLineEdit(QLineEdit):

    def __init__(self, backgroundColor = "#ffffff", cursor = QtCore.Qt.IBeamCursor,
                 font = QtGui.QFont("Glacial Indifference", 10), fontColor = "#5a5e5a",
                 maxLength = 20, parent = None):

        QLineEdit.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QLineEdit{background: %s; border: 1px solid #5a5e5a; \
                           border-radius: 5px; color: %s}" %(backgroundColor, fontColor))
        # Font
        self.setFont(font)
        # Max length
        self.setMaxLength(maxLength)
        
        
        
"""
ListWidget
"""
class KiangListWidget(QListWidget):

    def __init__(self, backgroundHoverColor = "#83e6d1",
                 backgroundSelectedColor = "#f98866", fontColor = "#5a5e5a",
                 fontSelectedColor = "#ffffff", parent = None):
        
        QListWidget.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("""QListWidget{color: %s; padding-top: 50px;
                            padding-left: 20px;}  QListView::item{border: none; 
                            border-radius: 5px; padding: 10px 5px 10px 5px;} 
                            QListView::item:hover{background: %s;}
                            QListView::item:selected{color: %s; border: 0;
                            outline: 0; background: %s;}""" %(fontColor, backgroundHoverColor,
                                                              fontSelectedColor, backgroundSelectedColor))
        # Cursor
        self.setCursor(QtCore.Qt.PointingHandCursor)
        # Focus
        self.setFocusPolicy(QtCore.Qt.NoFocus)

    def addItemList(self, itemList):

        if isinstance(itemList, QListWidgetItem):
            
            self.addItem(itemList)

        elif isinstance(itemList, list):

            for widgetItem in itemList:

                self.addItem(widgetItem)

        else:

            return



"""
ListWidgetItem
"""
class KiangListWidgetItem(QListWidgetItem):

    def __init__(self, text = "", font = QtGui.QFont("Glacial Indifference", 10),
                 icon = None, parent = None):

        QListWidgetItem.__init__(self, text, parent)
        # Set icon
        if icon:
            
            self.setIcon(icon)
            
        # Set font
        self.setFont(font)
        
        
"""
MainWindow
"""
class KiangMainWindow(QMainWindow):

    def __init__(self, backgroundColor = "#f5f5f5",
                 minSize = QtCore.QSize(900, 600), 
                 size = QtCore.QSize(1200, 800),
                 title = "Kiang", parent = None):

        QMainWindow.__init__(self, parent)
        # Background
        self.setStyleSheet("background: %s;" %backgroundColor)
        # Window title
        self.setWindowTitle(title)
        # Size of the window
        self.resize(size)
        # Minimum size
        self.setMinimumSize(minSize)
        # Centralwidget
        self.centralWidget = QWidget()
        # Set central widget
        self.setCentralWidget(self.centralWidget)
        # Show widget
        self.show()

    def setCentralWidgetLayout(self, layout):

        self.centralWidget.setLayout(layout)



"""
Splitter
"""
# Splitter
class KiangSplitter(QSplitter):

    def __init__(self, backgroundColor = "transparent", 
                 handleColor = "#4196a9",
                 direction = QtCore.Qt.Horizontal, 
                 parent = None):

        QSplitter.__init__(self, parent)
        # Orientation
        self.setOrientation(direction)
        # Stylesheet
        self.setStyleSheet("""QSplitter{background: %s} 
                           QSplitter::handle{background: %s}
                           QSplitter::handle:horizontal{width: 5px;}
                           QSplitter::handle:vertical{height: 5px;}""" %(backgroundColor, 
                                                                   handleColor))

    def addWidgetList(self, widgetList, stretchList):
        
        for index, widget in enumerate(widgetList):
            
            self.addWidget(widget)
            self.setStretchFactor(index, stretchList[index])
        
        

"""
SpinBox
"""
class KiangSpinBox(QSpinBox):
    
    def __init__(self, borderColor = "#5a5e5a",
                 cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 min = None, max = None, parent = None):
        
        QSpinBox.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("""QSpinBox{border: 1px solid %s; border-radius: 5px;} 
                              QSpinBox::up-button{border: none;} QSpinBox::down-button{border:none}  
                              QSpinBox::up-arrow{ image: url(./resources/images/uparrow_button.png); 
                              width: 10px; height: 10px;} 
                              QSpinBox::down-arrow{image: url(./resources/images/downarrow_button.png); 
                              width: 10px; height: 10px;}""" %borderColor)
        # Cusor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        # Set minimum and maximum
        if min:
            
            self.setMinimum(min)
            
        if max:
            
            self.setMaximum(max)
      
            

"""
Stackedwidget
"""
# StackedWidget
class KiangStackedWidget(QStackedWidget):

    def __init__(self, parent = None):

        QStackedWidget.__init__(self, parent)

    def addWidgetList(self, widgetList):

        if isinstance(widgetList, QWidget):

            self.addWidget(widgetList)

        elif isinstance(widgetList, list):
            
            for widget in widgetList:

                self.addWidget(widget)

        else:

            return

    def setStackIndex(self, index, animation = True):

        # If there is animation
        if animation:

            fader_widget = TransitionWidget(self.currentWidget(), 300, self.widget(index))
            del fader_widget
        
        self.setCurrentIndex(index)



"""
TextEdit
"""
class KiangTextEdit(QTextEdit):

    def __init__(self, backgroundColor = "#ffffff", 
                 cursor = QtCore.Qt.IBeamCursor,
                 font = QtGui.QFont("Glacial Indifference", 10),
                 fontColor = "#5a5e5a", parent = None):

        QTextEdit.__init__(self, parent)
        # Stylesheet
        self.setStyleSheet("QTextEdit{background: %s; color: %s}" %(backgroundColor, fontColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        self.setMinimumWidth(600)
        
        

"""
ToolBox
"""
class KiangToolBox(QToolBox):

    def __init__(self, backgroundColor = "transparent",
                 borderColor = "#60a92c",
                 borderSelectedColor = "#5a5e5a", 
                 cursor = QtCore.Qt.PointingHandCursor,
                 font = QtGui.QFont("Glacial Indifference", 10, QtGui.QFont.Bold),
                 fontColor = "#5a5e5a", 
                 parent = None):

        QToolBox.__init__(self, parent)
        self.setStyleSheet("""QToolBox{border: none;} 
                           QToolBox::tab{background: %s; 
                           border: none; border-bottom: 2px solid %s; color: %s;} 
                           QToolBox::tab:selected{border: none; 
                           border-bottom: 2px solid %s;}""" \
                           %(backgroundColor, borderColor, fontColor, 
                             borderSelectedColor))
        # Cursor
        self.setCursor(cursor)
        # Font
        self.setFont(font)
        
    # Add item to toolBox
    def addItemList(self, itemList, iconList = None, textList = None):

        # If there is one item
        if isinstance(itemList, QWidget):
            
            # If text is none, default ""
            if textList == None:
                
                textList = ""
                
            self.addItem(itemList, iconList, textList)

        elif isinstance(itemList, list):

            if iconList == None and textList == None:
                
                for widgetItem in itemList:
                    
                    self.addItem(widgetItem, "")
                    
            elif iconList == None:
                
                for index, widgetItem in enumerate(itemList):
                    
                    self.addItem(widgetItem, textList[index])
                
            elif textList == None:
                
                for index, widgetItem in enumerate(itemList):
                    
                    self.addItem(widgetItem, iconList[index], "")
              
            else:
                  
                for index, widgetItem in enumerate(itemList):
                 
                    self.addItem(widgetItem, iconList[index], textList[index])

        else:

            return        
        
        
