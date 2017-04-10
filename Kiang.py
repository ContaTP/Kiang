"""
Kiang --- A PyQt project to provide convienent access to data manipulation and plot
"""
# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import qtawesome as qta
# Python modules
import sys
import re
import csv
import pandas as pd
from io import StringIO

# Import widgets/function from other class
from widgets.ButtonGroup import KiangButtonGroup
from widgets.Frame import KiangFrame
from widgets.Label import KiangLabel
from widgets.Layout import KiangBoxLayout, KiangGridLayout
from widgets.LineEdit import KiangLineEdit
from widgets.ListWidget import KiangListWidget
from widgets.MainWindow import KiangMainWindow
from widgets.Messager import KiangMessager
from widgets.PushButton import KiangPushButton
from widgets.Splitter import KiangSplitter
from widgets.StackedWidget import KiangStackedWidget
from widgets.TextEdit import KiangTextEdit
from widgets.ToolBox import KiangToolBox
from widgets.ToolButton import KiangToolButton

# Import each module


from Animation import TransitionWidget



# Main application window
class KiangWindow(KiangMainWindow):

     def __init__(self, parent = None):

          # Init from KiangMainWindow
          super(KiangWindow, self).__init__()
          
          """Layout"""
          self.main_layout =  KiangBoxLayout(2, [0, 0, 0, 0], 10)
          super(KiangWindow, self).setCentralWidgetLayout(self.main_layout)

          """Widget"""
          # Menu and mainContent
          self.mainMenu_widget = KiangMenuWidget()
          self.mainContent_stackedWidget = KiangStackedWidget()
          # Children in stackedWidget
          self.dataLoad_widget = DataLoad()
          self.dataWarehouse_widget = DataWarehouse()
          self.graphMake_widget = GraphMakeWidget()
          self.setting_widget = SettingWidget()
          # Add widget to stackedWidget
          self.mainContent_stackedWidget.addWidget([self.dataLoad_widget, self.dataWarehouse_widget, self.graphMake_widget, self.setting_widget])
          # Add widget to layout
          self.main_layout.addWidget([self.mainMenu_widget, self.mainContent_stackedWidget], [1, 10])

          """Signal"""
          self.mainMenu_widget.indexChanged.connect(self.mainContent_stackedWidget.setStackIndex)


# Menu
class KiangMenuWidget(KiangFrame):

     # Signal
     indexChanged = QtCore.pyqtSignal(int)
     def __init__(self, parent = None):

          super(KiangMenuWidget, self).__init__("#2dd8b1")

          """Layout"""
          # Layout
          self.easyPlotMenu_layout = KiangBoxLayout(0, [0, 0, 0, 0], 0)
          
          """Widget"""
          # Button group
          self.easyPlot_buttonGroup = KiangButtonGroup()
          # Menu button
          self.fileLoad_button = KiangToolButton.menuToolButton("DATA", qta.icon("fa.cube", disabled = "fa.cubes",  color = "#ffffff", color_disabled ="#d82d54"))
          self.fileWarehouse_button = KiangToolButton.menuToolButton("WAREHOUSE", qta.icon("fa.database", disabled = "fa.database",  color = "#ffffff", color_disabled ="#d82d54"))
          self.graphMake_button = KiangToolButton.menuToolButton("GRAPH", qta.icon("fa.area-chart", color = "#ffffff", color_disabled ="#d82d54"))
          self.setting_button = KiangToolButton.menuToolButton("SETTING", qta.icon("fa.gear", disabled = "fa.gears", color = "#ffffff", color_disabled ="#d82d54"))
          # Add widget to button group
          self.easyPlot_buttonGroup.addButton([self.fileLoad_button, self.fileWarehouse_button, self.graphMake_button, self.setting_button])
          # Add widget
          self.easyPlotMenu_layout.addWidget([self.fileLoad_button, self.fileWarehouse_button, self.graphMake_button, self.setting_button])
          # Set layout
          self.setLayout(self.easyPlotMenu_layout)
          
          """Signal"""
          self.fileLoad_button.clicked.connect(self.__buttonClicked)
          self.fileWarehouse_button.clicked.connect(self.__buttonClicked)
          self.graphMake_button.clicked.connect(self.__buttonClicked)
          self.setting_button.clicked.connect(self.__buttonClicked)

     # Button clicked event
     """
     If a menu tab is clicked, disable the menu tab
     """
     def __buttonClicked(self):

          buttons = self.easyPlot_buttonGroup.buttons()
          index = self.easyPlot_buttonGroup.checkedId()
          for button in buttons:

               button.setDisabled(True) if self.easyPlot_buttonGroup.id(button) == index else button.setDisabled(False)

          self.indexChanged.emit(index)

         
# File load widget
class DataLoad(KiangFrame):

     def __init__(self, parent = None):

          super(DataLoad, self).__init__()

          """Layout"""
          self.dataLoad_layout = KiangBoxLayout(0, [5, 5, 5, 5], 15)

          """Widget"""
          # ListWidget for selecting data load method
          self.dataLoadMethod_listWidget = KiangListWidget()
          # Children of list widget
          self.pasteType_item = QtWidgets.QListWidgetItem(qta.icon("fa.paste", color = "#5a5e5a", color_active = "#ffffff"), "Paste")
          self.dragdropType_item = QtWidgets.QListWidgetItem(qta.icon("fa.file", color = "#5a5e5a", color_active = "#ffffff"), "Load a file")
          # Add children widget
          self.dataLoadMethod_listWidget.addItem([self.pasteType_item, self.dragdropType_item])
          # Stackedwidget
          self.dataLoadContent_stackedWidget  = KiangStackedWidget()
          # Children of stacked widget
          self.dataLoadPaste_widget = DataLoadPasteMethod()
          self.dataLoadDrag_widget = DataLoadDragMethod()
          # Add children widget
          self.dataLoadContent_stackedWidget.addWidget([self.dataLoadPaste_widget, self.dataLoadDrag_widget])
          # Add widget to layout
          self.dataLoad_layout.addWidget([self.dataLoadMethod_listWidget, self.dataLoadContent_stackedWidget],  [1, 5])                                                                                 
          # Set layout
          self.setLayout(self.dataLoad_layout)
          
          """Signal"""
          self.dataLoadMethod_listWidget.itemClicked.connect(self.__selectLoadMethod)

     def __selectLoadMethod(self, item):

          # Select the corresponding widget
          row = self.dataLoadMethod_listWidget.currentRow()
          self.dataLoadContent_stackedWidget.setCurrentIndex(row)


class DataLoadPasteMethod(KiangFrame):

     def __init__(self, parent = None):

          # Init
          super(DataLoadPasteMethod, self).__init__()

          """Layout"""
          self.dataLoadPaste_layout = KiangGridLayout(0)

          """Main Widget"""
          # Message area
          self.dataLoadPasteMessage_widget = KiangMessager()
          # Textedit
          self.dataLoadPaste_textEdit = KiangTextEdit()
          # Toolbox
          self.dataLoadPaste_toolBox = KiangToolBox()
          # Launch button
          self.dataLoadPasteRun_pushButton = KiangPushButton(icon = qta.icon("fa.rocket", color = "#ffffff"), text = "ADD TO WAREHOUSE")

          """ToolBox Widget"""
          # Layout
          self.dataLoadPasteData_widget = KiangFrame()
          self.dataLoadPasteData_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
          
          # Filename
          self.dataLoadPasteDataFilename_label = KiangLabel("Data name")
          self.dataLoadPasteDataFilename_lineEdit = KiangLineEdit()

          # Delimiter
          self.dataLoadPasteDataDelimiter_label = KiangLabel("Delimiter")
          # Groupbox for delimiter
          self.dataLoadPasteDataDelimiter_groupBox =  KiangGroupBox()
          # Groupbox layout
          self.dataLoadPasteDataDelimiter_groupBoxLayout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
          
          # Button group for delimiter
          self.dataLoadPasteDataDelimiter_buttonGroup = KiangButtonGroup()
          # Each button
          self.fileLoadPasteDataDelimiter_commaRadioButton = QtWidgets.QRadioButton("Comma")
          self.fileLoadPasteDataDelimiter_commaRadioButton.setChecked(True)
          self.fileLoadPasteDataDelimiter_semicolonRadioButton = QtWidgets.QRadioButton("Semicolon")
          self.fileLoadPasteDataDelimiter_spaceRadioButton = QtWidgets.QRadioButton("Space")
          self.fileLoadPasteDataDelimiter_tabRadioButton = QtWidgets.QRadioButton("Tab")
          # Set font
          self.fileLoadPasteDataDelimiter_commaRadioButton.setFont(font)
          self.fileLoadPasteDataDelimiter_semicolonRadioButton.setFont(font)
          self.fileLoadPasteDataDelimiter_spaceRadioButton.setFont(font)
          self.fileLoadPasteDataDelimiter_tabRadioButton.setFont(font)
          # Add button to groupbox and  buttongroup
          self.fileLoadPasteDataDelimiter_groupBoxLayout.addWidget(self.fileLoadPasteDataDelimiter_commaRadioButton, 1)
          self.fileLoadPasteDataDelimiter_groupBoxLayout.addWidget(self.fileLoadPasteDataDelimiter_semicolonRadioButton, 1)
          self.fileLoadPasteDataDelimiter_groupBoxLayout.addWidget(self.fileLoadPasteDataDelimiter_spaceRadioButton, 1)
          self.fileLoadPasteDataDelimiter_groupBoxLayout.addWidget(self.fileLoadPasteDataDelimiter_tabRadioButton, 1)
          self.fileLoadPasteDataDelimiter_buttonGroup.addButton(self.fileLoadPasteDataDelimiter_commaRadioButton, 0)
          self.fileLoadPasteDataDelimiter_buttonGroup.addButton(self.fileLoadPasteDataDelimiter_semicolonRadioButton, 1)
          self.fileLoadPasteDataDelimiter_buttonGroup.addButton(self.fileLoadPasteDataDelimiter_spaceRadioButton, 2)
          self.fileLoadPasteDataDelimiter_buttonGroup.addButton(self.fileLoadPasteDataDelimiter_tabRadioButton, 3)
          # Set layout to button group
          self.fileLoadPasteDataDelimiter_groupBox.setLayout(self.fileLoadPasteDataDelimiter_groupBoxLayout)
          # Statistics
          self.fileLoadPasteDataStatistics_label = KiangLabel("Statistics")
          self.fileLoadPasteDataStatistics_label.setHidden(True)
          self.fileLoadPasteDataStatistics_groupBox = QtWidgets.QGroupBox("")
          self.fileLoadPasteDataStatistics_groupBox.setStyleSheet("QGroupBox{border: none; color: #5a5e5a;} QRadioButton{color:#5a5e5a;}")
          self.fileLoadPasteDataStatistics_groupBox.setFont(font)
          self.fileLoadPasteDataStatistics_groupBox.setHidden(True)
          # Groupbox layout
          self.fileLoadPasteDataStatistics_groupBoxLayout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
          # Statistics label
          self.fileLoadPasteDataStatisticsNrow_label = KiangLabel("")
          self.fileLoadPasteDataStatisticsNcol_label = KiangLabel("")
          self.fileLoadPasteDataStatisticsMissing_label = KiangLabel("")
          # Add label to layout
          self.fileLoadPasteDataStatistics_groupBoxLayout.addWidget(self.fileLoadPasteDataStatisticsNrow_label, 1)
          self.fileLoadPasteDataStatistics_groupBoxLayout.addWidget(self.fileLoadPasteDataStatisticsNcol_label, 1)
          self.fileLoadPasteDataStatistics_groupBoxLayout.addWidget(self.fileLoadPasteDataStatisticsMissing_label, 1)
          # Set layout to label group
          self.fileLoadPasteDataStatistics_groupBox.setLayout(self.fileLoadPasteDataStatistics_groupBoxLayout)
          # Add widgets to layout
          self.fileLoadPasteData_layout.addWidget(self.fileLoadPasteDataFilename_label)
          self.fileLoadPasteData_layout.addWidget(self.fileLoadPasteDataFilename_lineEdit)
          self.fileLoadPasteData_layout.addWidget(self.fileLoadPasteDataDelimiter_label)
          self.fileLoadPasteData_layout.addWidget(self.fileLoadPasteDataDelimiter_groupBox)
          self.fileLoadPasteData_layout.addWidget(self.fileLoadPasteDataStatistics_label)
          self.fileLoadPasteData_layout.addWidget(self.fileLoadPasteDataStatistics_groupBox)
          self.fileLoadPasteData_layout.addStretch(1)
          # Set layout
          self.fileLoadPasteData_widget.setLayout(self.fileLoadPasteData_layout)

          # Row
          # Layout
          self.fileLoadPasteRow_widget = QtWidgets.QFrame()
          self.fileLoadPasteRow_layout = QtWidgets.QVBoxLayout()
          # Checkbox for first row as header
          self.fileLoadPasteRowFirstheader_label = QtWidgets.QLabel("Header")
          self.fileLoadPasteRowFirstheader_label.setFont(font)
          self.fileLoadPasteRowFirstheader_checkBox = QtWidgets.QCheckBox("First row as header")
          self.fileLoadPasteRowFirstheader_checkBox.setChecked(True)
          self.fileLoadPasteRowFirstheader_checkBox.setFont(font)
          # Range
          self.fileLoadPasteRowRange_label = QtWidgets.QLabel("Row Range")
          self.fileLoadPasteRowRange_label.setFont(font)
          self.fileLoadPasteRowRange_label.setHidden(True)
          self.fileLoadPasteRowRange_widget = QtWidgets.QFrame()
          self.fileLoadPasteRowRange_widget.setHidden(True)
          # Layout
          self.fileLoadPasteRowRange_layout = QtWidgets.QGridLayout()
          # Widgets
          self.fileLoadPasteRowRangeMin_label =  QtWidgets.QLabel("Min:")
          self.fileLoadPasteRowRangeMin_label.setFont(font)
          self.fileLoadPasteRowRangeMin_spinBox = QtWidgets.QSpinBox()
          self.fileLoadPasteRowRangeMin_spinBox.setStyleSheet("QSpinBox{border: 1px solid #5a5e5a; border-radius: 5px;} QSpinBox::up-button{border: none;} QSpinBox::down-button{border:none}  QSpinBox::up-arrow{ image: url(./resources/images/uparrow_button.png); width: 10px; height: 10px;} QSpinBox::down-arrow{image: url(./resources/images/downarrow_button.png); width: 10px; height: 10px;}")
          self.fileLoadPasteRowRangeMin_spinBox.setFont(font)
          self.fileLoadPasteRowRangeMin_spinBox.setMinimum(1)
          self.fileLoadPasteRowRangeMax_label = QtWidgets.QLabel("Max:")
          self.fileLoadPasteRowRangeMax_label.setFont(font)
          self.fileLoadPasteRowRangeMax_spinBox = QtWidgets.QSpinBox()
          self.fileLoadPasteRowRangeMax_spinBox.setStyleSheet("QSpinBox{border: 1px solid #5a5e5a; border-radius: 5px;} QSpinBox::up-button{border: none;} QSpinBox::down-button{border:none} QSpinBox::up-arrow{ image: url(./resources/images/uparrow_button.png); width: 10px; height: 10px;} QSpinBox::down-arrow{image: url(./resources/images/downarrow_button.png); width: 10px; height: 10px;}")
          self.fileLoadPasteRowRangeMax_spinBox.setFont(font)
          """ Users need to select at least two rows in the data """
          self.fileLoadPasteRowRangeMax_spinBox.setMinimum(2)
          # Add item to layout
          self.fileLoadPasteRowRange_layout.addWidget(self.fileLoadPasteRowRangeMin_label , 0, 0, 1, 1)
          self.fileLoadPasteRowRange_layout.addWidget(self.fileLoadPasteRowRangeMin_spinBox, 0, 1, 1, 1)
          self.fileLoadPasteRowRange_layout.addWidget(self.fileLoadPasteRowRangeMax_label , 1, 0, 1, 1)
          self.fileLoadPasteRowRange_layout.addWidget(self.fileLoadPasteRowRangeMax_spinBox, 1, 1, 1, 1)
          # Set layout to the widget
          self.fileLoadPasteRowRange_widget.setLayout(self.fileLoadPasteRowRange_layout)
          # Add widgets to layout
          self.fileLoadPasteRow_layout.addWidget(self.fileLoadPasteRowFirstheader_label)
          self.fileLoadPasteRow_layout.addWidget(self.fileLoadPasteRowFirstheader_checkBox)
          self.fileLoadPasteRow_layout.addWidget(self.fileLoadPasteRowRange_label)
          self.fileLoadPasteRow_layout.addWidget(self.fileLoadPasteRowRange_widget)
          self.fileLoadPasteRow_layout.addStretch(1)
          # Set layout
          self.fileLoadPasteRow_widget.setLayout(self.fileLoadPasteRow_layout)


          # Col
          # Layout
          self.fileLoadPasteCol_widget = QtWidgets.QFrame()
          self.fileLoadPasteCol_layout = QtWidgets.QVBoxLayout()
          # Checkbox for first col as index
          self.fileLoadPasteColFirstindex_label = QtWidgets.QLabel("Index")
          self.fileLoadPasteColFirstindex_label.setFont(font)
          self.fileLoadPasteColFirstindex_checkBox = QtWidgets.QCheckBox("First column as index")
          self.fileLoadPasteColFirstindex_checkBox.setChecked(False)
          self.fileLoadPasteColFirstindex_checkBox.setFont(font)
          # Range
          self.fileLoadPasteColRange_label = QtWidgets.QLabel("Column Range")
          self.fileLoadPasteColRange_label.setFont(font)
          self.fileLoadPasteColRange_label.setHidden(True)
          self.fileLoadPasteColRange_widget = QtWidgets.QFrame()
          self.fileLoadPasteColRange_widget.setHidden(True)
          # Layout
          self.fileLoadPasteColRange_layout = QtWidgets.QGridLayout()
          # Widgets
          self.fileLoadPasteColRangeMin_label =  QtWidgets.QLabel("Min:")
          self.fileLoadPasteColRangeMin_label.setFont(font)
          self.fileLoadPasteColRangeMin_spinBox = QtWidgets.QSpinBox()
          self.fileLoadPasteColRangeMin_spinBox.setStyleSheet("QSpinBox{border: 1px solid #5a5e5a; border-radius: 5px;} QSpinBox::up-button{border: none;} QSpinBox::down-button{border:none}  QSpinBox::up-arrow{ image: url(./resources/images/uparrow_button.png); width: 10px; height: 10px;} QSpinBox::down-arrow{image: url(./resources/images/downarrow_button.png); width: 10px; height: 10px;}")
          self.fileLoadPasteColRangeMin_spinBox.setFont(font)
          self.fileLoadPasteColRangeMin_spinBox.setMinimum(1)
          self.fileLoadPasteColRangeMax_label = QtWidgets.QLabel("Max:")
          self.fileLoadPasteColRangeMax_label.setFont(font)
          self.fileLoadPasteColRangeMax_spinBox = QtWidgets.QSpinBox()
          self.fileLoadPasteColRangeMax_spinBox.setStyleSheet("QSpinBox{border: 1px solid #5a5e5a; border-radius: 5px;} QSpinBox::up-button{border: none;} QSpinBox::down-button{border:none} QSpinBox::up-arrow{ image: url(./resources/images/uparrow_button.png); width: 10px; height: 10px;} QSpinBox::down-arrow{image: url(./resources/images/downarrow_button.png); width: 10px; height: 10px;}")
          self.fileLoadPasteColRangeMax_spinBox.setFont(font)
          """ Users can select only one variable from the data """
          self.fileLoadPasteColRangeMax_spinBox.setMinimum(1)
          # Add item to layout
          self.fileLoadPasteColRange_layout.addWidget(self.fileLoadPasteColRangeMin_label , 0, 0, 1, 1)
          self.fileLoadPasteColRange_layout.addWidget(self.fileLoadPasteColRangeMin_spinBox, 0, 1, 1, 1)
          self.fileLoadPasteColRange_layout.addWidget(self.fileLoadPasteColRangeMax_label , 1, 0, 1, 1)
          self.fileLoadPasteColRange_layout.addWidget(self.fileLoadPasteColRangeMax_spinBox, 1, 1, 1, 1)
          # Set layout to the widget
          self.fileLoadPasteColRange_widget.setLayout(self.fileLoadPasteColRange_layout)
          # Add widgets to layout
          self.fileLoadPasteCol_layout.addWidget(self.fileLoadPasteColFirstindex_label)
          self.fileLoadPasteCol_layout.addWidget(self.fileLoadPasteColFirstindex_checkBox)
          self.fileLoadPasteCol_layout.addWidget(self.fileLoadPasteColRange_label)
          self.fileLoadPasteCol_layout.addWidget(self.fileLoadPasteColRange_widget)
          self.fileLoadPasteCol_layout.addStretch(1)
          # Add widget
          self.fileLoadPasteCol_widget.setLayout(self.fileLoadPasteCol_layout)

          # Missing
          self.fileLoadPasteMissing_widget = QtWidgets.QFrame()
          self.fileLoadPasteMissing_widget.setEnabled(False)
          # Layout
          self.fileLoadPasteMissing_layout = QtWidgets.QVBoxLayout()
          # Label
          self.fileLoadPasteMissingObsolete_label = QtWidgets.QLabel("Missing Cells")
          self.fileLoadPasteMissingObsolete_label.setFont(font)
          # Groupbox
          self.fileLoadPasteMissingObsolete_groupBox = QtWidgets.QGroupBox("")
          self.fileLoadPasteMissingObsolete_groupBox.setStyleSheet("QGroupBox{border: none; color: #5a5e5a;} QRadioButton{color:#5a5e5a;}")
          self.fileLoadPasteMissingObsolete_groupBox.setFont(font)
          # Layout
          self.fileLoadPasteMissingObsoleteGroupBox_layout = QtWidgets.QVBoxLayout()
          # Buttongroup
          self.fileLoadPasteMissingObsolete_buttonGroup = QtWidgets.QButtonGroup()
          # Radiobutton
          self.fileLoadPasteMissingObsolete_radioButton = QtWidgets.QRadioButton("Delete")
          self.fileLoadPasteMissingObsolete_radioButton.setFont(font)
          self.fileLoadPasteMissingKeep_radioButton = QtWidgets.QRadioButton("Keep all")
          self.fileLoadPasteMissingKeep_radioButton.setFont(font)
          self.fileLoadPasteMissingKeep_radioButton.setChecked(True)
          self.fileLoadPasteMissingKeepOnly_radioButton = QtWidgets.QRadioButton("Keep missing only")
          self.fileLoadPasteMissingKeepOnly_radioButton.setFont(font)          
          # Add radiobox to layout
          self.fileLoadPasteMissingObsoleteGroupBox_layout.addWidget(self.fileLoadPasteMissingObsolete_radioButton)
          self.fileLoadPasteMissingObsoleteGroupBox_layout.addWidget(self.fileLoadPasteMissingKeep_radioButton)
          self.fileLoadPasteMissingObsoleteGroupBox_layout.addWidget(self.fileLoadPasteMissingKeepOnly_radioButton)
          self.fileLoadPasteMissingObsolete_buttonGroup.addButton(self.fileLoadPasteMissingObsolete_radioButton, 0)
          self.fileLoadPasteMissingObsolete_buttonGroup.addButton(self.fileLoadPasteMissingKeep_radioButton, 1)
          self.fileLoadPasteMissingObsolete_buttonGroup.addButton(self.fileLoadPasteMissingKeepOnly_radioButton, 2)
          # Set layout to groupBox
          self.fileLoadPasteMissingObsolete_groupBox.setLayout(self.fileLoadPasteMissingObsoleteGroupBox_layout)
          # Add item to layout
          self.fileLoadPasteMissing_layout.addWidget(self.fileLoadPasteMissingObsolete_label)
          self.fileLoadPasteMissing_layout.addWidget(self.fileLoadPasteMissingObsolete_groupBox)
          self.fileLoadPasteMissing_layout.addStretch(1)
          # Set layout
          self.fileLoadPasteMissing_widget.setLayout(self.fileLoadPasteMissing_layout)
          
          # Add item to toolbox
          self.fileLoadPaste_toolBox.addItem(self.fileLoadPasteData_widget, qta.icon("fa.heartbeat", color = "#5a5e5a"),  "DATA")
          self.fileLoadPaste_toolBox.addItem(self.fileLoadPasteRow_widget, qta.icon("fa.list-ol", color = "#5a5e5a"), "ROWS")
          self.fileLoadPaste_toolBox.addItem(self.fileLoadPasteCol_widget, qta.icon("fa.columns", color = "#5a5e5a"), "COLUMNS")
          self.fileLoadPaste_toolBox.addItem(self.fileLoadPasteMissing_widget, qta.icon("fa.paw", color = "#5a5e5a"), "MISSING")
          # Add widget to splitter
          self.fileLoadPasteTool_layout.addWidget([self.fileLoadPaste_toolBox, self.fileLoadPasteRun_pushButton], [15, 1])
          self.fileLoadPasteTool_widget.setLayout(self.fileLoadPasteTool_layout)
          # Splitter
          self.dataLoadPaste_splitter = KiangSplitter(QtCore.Qt.Horizontal)
          self.fileLoadPaste_splitter.addWidget(self.fileLoadPaste_textEdit)
          self.fileLoadPaste_splitter.addWidget(self.fileLoadPasteTool_widget)
          # Stretch factor in splitter
          self.fileLoadPaste_splitter.setStretchFactor(0, 2)
          self.fileLoadPaste_splitter.setStretchFactor(1, 1)
          # Add widget to layout
          self.fileLoadPaste_layout.addWidget(self.fileLoadPaste_splitter)
          # Set layout
          self.setLayout(self.fileLoadPaste_layout)


          # Variable
          # Shape
          self.shape = [0, 0]
          # Dict for delimiter
          self.dataDelimiter_dict = {0: ",", 1: ";", 2: " ", 3: "\t"}
          # Default delimiter is comma
          self.dataDelimiter = self.dataDelimiter_dict[0]
          # Filename
          self.dataFilename = ""
          # First row as header
          self.firstRowAsHeader = True
          # First col as index
          self.firstColAsIndex = False
          # Count of missing cells
          self.missingCount = 0
          # Missing value
          self.missingObsolete = False
          # Default keep all
          self.missingObsoleteOption = 1

          """Variable"""
          self.parent = parent
     
          """Signal"""
          self.fileLoadPaste_textEdit.textChanged.connect(self.getData)
          self.fileLoadPasteDataDelimiter_tabRadioButton.toggled.connect(self.getDelimiter)
          self.fileLoadPasteDataDelimiter_commaRadioButton.toggled.connect(self.getDelimiter)
          self.fileLoadPasteDataDelimiter_semicolonRadioButton.toggled.connect(self.getDelimiter)
          self.fileLoadPasteDataDelimiter_spaceRadioButton.toggled.connect(self.getDelimiter)
          self.fileLoadPasteRowFirstheader_checkBox.toggled.connect(self.setHeader)
          self.fileLoadPasteRowRangeMin_spinBox.valueChanged.connect(self.setRowRangeMinValue)
          self.fileLoadPasteRowRangeMax_spinBox.valueChanged.connect(self.setRowRangeMaxValue)
          self.fileLoadPasteColFirstindex_checkBox.toggled.connect(self.setIndex)
          self.fileLoadPasteColRangeMin_spinBox.valueChanged.connect(self.setColRangeMinValue)
          self.fileLoadPasteColRangeMax_spinBox.valueChanged.connect(self.setColRangeMaxValue)
          self.fileLoadPasteMissingObsolete_radioButton.toggled.connect(self.getMissing)
          self.fileLoadPasteMissingKeep_radioButton.toggled.connect(self.getMissing)
          self.fileLoadPasteMissingKeepOnly_radioButton.toggled.connect(self.getMissing)
          # self.fileLoadPasteDataFilename_lineEdit.textChanged.connect(self.getFilename)


     # Obtain the delimiter from the interface
     def getDelimiter(self, toggledOn):

          # If toggled off signal, return
          if not toggledOn:

               return
          
          checked_id = self.fileLoadPasteDataDelimiter_buttonGroup.checkedId()
          self.dataDelimiter = self.dataDelimiter_dict[checked_id]
          # Everytime checked a new radio button, read the data again
          self.getData()

     # Obtain data
     def getData(self):

          # If not space delimiter, strip all the space
          if self.dataDelimiter != " ":
               
               text = self.fileLoadPaste_textEdit.toPlainText().replace(" ", "")

          else:

               text = self.fileLoadPaste_textEdit.toPlainText()

          # If this is the first line, skipped
          if "\n" not in text:

               return
          
          buffer = StringIO(text)
          header = 0 if self.firstRowAsHeader else None
          row_index = 0 if self.firstColAsIndex else False
          try:

                # Index_col is set to false as default
                reader = pd.io.parsers.read_csv(buffer, delimiter = self.dataDelimiter, header = header, index_col = row_index)
                msg = ""
                self.messageSent.emit(msg, "VoidMessager")

          except pd.parser.CParserError:

               msg = "Cannot parse the data !"
               self.messageSent.emit(msg, "ErrorMessager")
               reader = pd.DataFrame()

          except IndexError:

               msg = "Index out of range !"
               self.messageSent.emit(msg, "ErrorMessager")
               reader = pd.DataFrame()

          # Get statistics
          self.shape = reader.shape
          self.missingCount = reader.isnull().values.ravel().sum()
          if self.shape[0] > 1:

                self.fileLoadPasteDataStatisticsNrow_label.setText("Rows:%s"% (self.shape[0]))
                self.fileLoadPasteDataStatisticsNcol_label.setText("Cols:%s"% (self.shape[1]))
                self.fileLoadPasteDataStatisticsMissing_label.setText("Missing cells: %s"% (self.missingCount))
                self.showStatistics(True)
                self.showRowRange(True)
                self.showColRange(True)
                self.showMissing(self.missingCount > 0)

          else:

               self.showStatistics(False)
               self.showRowRange(False)
               self.showColRange(False)
               self.showMissing(False)
                    
     def getFilename(self):

          # Get filename and replace the space with underscore
          filename = self.fileLoadPasteDataFilename_lineEdit.text().replace(" ", "_")

     def getMissing(self):

          # Get missing
          self.missingObsoleteOption = self.fileLoadPasteMissingObsolete_buttonGroup.checkedId()
          

     # Set the range for row min
     def setColRangeMinValue(self):

          # Get values 
          minValue = int(self.fileLoadPasteColRangeMin_spinBox.value())
          maxValue = int(self.fileLoadPasteColRangeMax_spinBox.value())
          if maxValue < minValue:

               self.fileLoadPasteColRangeMax_spinBox.setValue(minValue)
               
     # Set the range for row max
     def setColRangeMaxValue(self):

          # Get values 
          minValue = int(self.fileLoadPasteColRangeMin_spinBox.value())
          maxValue = int(self.fileLoadPasteColRangeMax_spinBox.value())
          if maxValue < minValue:

               self.fileLoadPasteColRangeMin_spinBox.setValue(maxValue)
               
     # Set header
     def setHeader(self, toggledOn):

          self.firstRowAsHeader = True if toggledOn == True else False
          self.getData()

     # Index
     def setIndex(self, toggledOn):

          self.firstColAsIndex = True if toggledOn == True else False
          self.getData()
          
     # Set the range for row min
     def setRowRangeMinValue(self):

          # Get values 
          minValue = int(self.fileLoadPasteRowRangeMin_spinBox.value())
          maxValue = int(self.fileLoadPasteRowRangeMax_spinBox.value())
          if maxValue <= minValue:

               self.fileLoadPasteRowRangeMax_spinBox.setValue(minValue + 1)
               
     # Set the range for row max
     def setRowRangeMaxValue(self):

          # Get values 
          minValue = int(self.fileLoadPasteRowRangeMin_spinBox.value())
          maxValue = int(self.fileLoadPasteRowRangeMax_spinBox.value())
          if maxValue <= minValue:

               self.fileLoadPasteRowRangeMin_spinBox.setValue(maxValue - 1)

     # Functions to show the column range
     def showColRange(self, showFlag):

          self.fileLoadPasteColRange_label.setVisible(showFlag)
          self.fileLoadPasteColRange_widget.setVisible(showFlag)
          maxAllowed = 1 if self.shape[1] == 1 else self.shape[1]
          self.fileLoadPasteColRangeMin_spinBox.setMaximum(maxAllowed)
          self.fileLoadPasteColRangeMax_spinBox.setMaximum(maxAllowed)
          self.fileLoadPasteColRangeMin_spinBox.setValue(1)
          self.fileLoadPasteColRangeMax_spinBox.setValue(maxAllowed)

     # Funcions to show the missing data tab
     def showMissing(self, showFlag):

          self.fileLoadPasteMissing_widget.setEnabled(showFlag)
          
     # Functions to show the statistics
     def showStatistics(self, showFlag):

          self.fileLoadPasteDataStatistics_label.setVisible(showFlag)
          self.fileLoadPasteDataStatistics_groupBox.setVisible(showFlag)


     # Functions to show the row range
     def showRowRange(self, showFlag):

          self.fileLoadPasteRowRange_label.setVisible(showFlag)
          self.fileLoadPasteRowRange_widget.setVisible(showFlag)
          maxAllowed = 2 if self.shape[0] <= 2 else self.shape[0]
          self.fileLoadPasteRowRangeMin_spinBox.setMaximum(maxAllowed - 1)
          self.fileLoadPasteRowRangeMax_spinBox.setMaximum(maxAllowed)
          self.fileLoadPasteRowRangeMin_spinBox.setValue(1)
          self.fileLoadPasteRowRangeMax_spinBox.setValue(maxAllowed)
               
               


class DataLoadDragMethod(QtWidgets.QFrame):

     def __init__(self, parent = None):
      
          QtWidgets.QFrame.__init__(self, parent)
          # Stylesheet
          self.setStyleSheet("background: #eeeeee; border: 2px dashed #5a5e5a")
          # Set cursor
          self.setCursor(QtCore.Qt.PointingHandCursor)
          # Accept drops
          self.setAcceptDrops(True)

     def  dragEnterEvent(self, event):

          event.accept()

     def dragLeaveEvent(self, event):

          event.accept()
         
     def dragMoveEvent(self, event):

          event.accept()

     def dropEvent(self, event):

          data = event.mimeData()
          urls = data.urls()
        
     def mousePressEvent(self, event):

          dialog = QtWidgets.QFileDialog()
          dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
          self.inputfile, filetype = dialog.getOpenFileName(self, "Open", "", "CSV(*.csv);;Excel(*.xls,xlsx)")


class FileLoadViewWidget(QtWidgets.QFrame):

     def __init__(self, parent = None):

          QtWidgets.QFrame.__init__(self, parent)
          # Add widget
          self.fileLoadView_layout.addWidget(self.fileLoadViewToolBox_widget)
          self.fileLoadView_layout.addWidget(self.fileLoadViewLaunch_button)
          # Set layout
          self.setLayout(self.fileLoadView_layout)

class FileLoadViewDataWidget(QtWidgets.QFrame):

     def __init__(self, parent = None):

          QtWidgets.QFrame.__init__(self, parent)

class DataWarehouse(QtWidgets.QFrame):

     def __init__(self, parent = None):

          QtWidgets.QFrame.__init__(self, parent)
     
class GraphMakeWidget(QtWidgets.QFrame):

     def __init__(self, parent = None):

          QtWidgets.QFrame.__init__(self, parent)


class SettingWidget(QtWidgets.QFrame):

     def __init__(self, parent = None):

          QtWidgets.QFrame.__init__(self, parent)

          
# Main function
# The main function if started from Python
def main():
    
    # Set a unique id to BATS
    import ctypes
    appid = u'EasyPlot.0.0.1'
    # Check the platform. If windows, set an ID so it will be in the task bar.
    if sys.platform == 'win32':

       ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    
    elif sys.platform == 'linux':

       pass

    elif sys.platform == 'darwin':

        pass
    
    else:
      
      sys.stdout.write("The application is not supported in this system")
      pass
    # Create the application
    app = QtWidgets.QApplication(['EasyPlot'])
    # Add icon for the application
    # Add font to the font database
    QtGui.QFontDatabase().addApplicationFont(":/resources/font/manteka.ttf")
    QtGui.QFontDatabase().addApplicationFont(":/resources/font/FredokaOne-Regular.ttf")
    QtGui.QFontDatabase().addApplicationFont(":/resources/font/GlacialIndifference-Regular.otf")
    QtGui.QFontDatabase().addApplicationFont(":/resources/font/GlacialIndifference-Bold.otf")
    # Initialize the GUI
    window = KiangWindow()
    window.show()
    # Run the app
    sys.exit(app.exec_())


# Initialize of the app
if __name__ == '__main__':
    
    # The main function
    main()
