"""
Kiang --- A PyQt project to provide convenient access to data manipulation and plot
"""
# PyQt5 module
from PyQt5 import QtCore, QtGui, QtWidgets
# Font awesome
import qtawesome as qta
# Python modules
import sys
import re
import csv
import pandas as pd
from io import StringIO

# Import widgets/function from other class
from widgets.Button import KiangPushButton, KiangRadioButton, KiangToolButton
from widgets.ButtonGroup import KiangButtonGroup
from widgets.CheckBox import KiangCheckBox
from widgets.Frame import KiangFrame
from widgets.GroupBox import KiangGroupBox
from widgets.Label import KiangLabel
from widgets.Layout import KiangBoxLayout, KiangGridLayout
from widgets.LineEdit import KiangLineEdit
from widgets.ListWidget import KiangListWidget, KiangListWidgetItem
from widgets.MainWindow import KiangMainWindow
from widgets.Messager import KiangMessager
from widgets.SpinBox import KiangSpinBox
from widgets.Splitter import KiangSplitter
from widgets.StackedWidget import KiangStackedWidget
from widgets.TextEdit import KiangTextEdit
from widgets.ToolBox import KiangToolBox

# Import each module
from Animation import TransitionWidget



# Main application window
class KiangWindow(KiangMainWindow):

    def __init__(self, parent = None):

        # Init from KiangMainWindow
        super(KiangWindow, self).__init__()
        
        """Layout"""
        self.main_layout =  KiangBoxLayout(2, [0, 0, 0, 0], 10)
        # Set central widget
        super(KiangWindow, self).setCentralWidgetLayout(self.main_layout)
        
        
        """Widget"""
        """Menu Widget"""
        # Menu
        self.mainMenu_widget = KiangFrame()
        self.mainMenu_buttonGroup = KiangButtonGroup()
        # Menu layout
        self.mainMenu_layout = KiangBoxLayout(0, [0, 0, 0, 0], 0)        
        # Menu button
        self.import_button = KiangToolButton.menuToolButton("DATA", qta.icon("fa.cube", color = "#ffffff", 
                                                                             color_disabled ="#d82d54", disabled = "fa.cubes"))
        self.view_button = KiangToolButton.menuToolButton("WAREHOUSE", qta.icon("fa.database", color = "#ffffff", 
                                                                                color_disabled ="#d82d54", disabled = "fa.database"))
        self.plot_button = KiangToolButton.menuToolButton("GRAPH", qta.icon("fa.area-chart", color = "#ffffff", 
                                                                            color_disabled ="#d82d54", disabled = "fa.area-chart"))
        self.setting_button = KiangToolButton.menuToolButton("SETTING", qta.icon("fa.gear", color = "#ffffff", 
                                                                                 color_disabled ="#d82d54", disabled = "fa.gears"))
        # Add menu button to menu buttonGroup
        self.mainMenu_buttonGroup.addButton([self.import_button, self.view_button, 
                                            self.plot_button, self.setting_button])
        # Add widget to menu layout
        self.mainMenu_layout.addWidget([self.import_button, self.view_button, 
                                        self.plot_button, self.setting_button])
        # Set layout
        self.mainMenu_widget.setLayout(self.mainMenu_layout)        
        
        """Main Content Widget"""
        # Main content
        self.mainContent_stackedWidget = KiangStackedWidget()
        # Children in stackedWidget
        self.import_widget = ImportData()
        self.view_widget = DataWarehouse()
        self.plot_widget = GraphMakeWidget()
        self.setting_widget = SettingWidget()
        # Add widget to stackedWidget
        self.mainContent_stackedWidget.addWidget([self.import_widget, self.view_widget, 
                                                  self.plot_widget, self.setting_widget])
        
        
        # Add widget to layout
        self.main_layout.addWidget([self.mainMenu_widget, self.mainContent_stackedWidget], [1, 10])
        
        
        """Signal"""
        self.import_button.clicked.connect(self.__buttonClicked)
        self.view_button.clicked.connect(self.__buttonClicked)
        self.plot_button.clicked.connect(self.__buttonClicked)
        self.setting_button.clicked.connect(self.__buttonClicked)


    # Button clicked event
    """
    When a menu tab is clicked, disable the clicked menu tab
    """
    def __buttonClicked(self):

        buttons = self.mainMenu_buttonGroup.buttons()
        index = self.mainMenu_buttonGroup.checkedId()
        for button in buttons:

            button.setDisabled(True) if self.mainMenu_buttonGroup.id(button) == index else button.setDisabled(False)

        self.mainContent_stackedWidget.setStackIndex(index)

         
# File load widget
class ImportData(KiangFrame):

    def __init__(self, parent = None):

        super(ImportData, self).__init__()

        """Layout"""
        self.import_layout = KiangBoxLayout(0, [5, 5, 5, 5], 15)
        
        """Widget"""
        # ListWidget for selecting data load method
        self.importMethod_listWidget = KiangListWidget()
        # Children of list widget
        # Import method: paste, drag & drop, url (future)
        self.paste_listItem = KiangListWidgetItem(qta.icon("fa.paste", color = "#5a5e5a", 
                                                           color_active = "#ffffff"), "Paste")
        self.drag_listItem = KiangListWidgetItem(qta.icon("fa.file", color = "#5a5e5a", 
                                                          color_active = "#ffffff"), "Load a file")
        # Children widget
        # Listwidget of the vertical menu to choose the import method
        self.importMethod_listWidget.addItem([self.paste_listItem, self.drag_listItem])
        # Stackedwidget of content
        self.importContent_stackedWidget  = KiangStackedWidget()
        # Children of stacked widget
        self.paste_widget = ImportPasteMethod()
        self.drag_widget = ImportDragMethod()
        # Add children widget
        self.importContent_stackedWidget.addWidget([self.paste_widget, self.drag_widget])
        # Add widget to layout
        self.import_layout.addWidget([self.importMethod_listWidget, self.importContent_stackedWidget],  [1, 5])                                                                                 
        # Set layout
        self.setLayout(self.import_layout)
        
        """Signal"""
        self.importMethod_listWidget.itemClicked.connect(self.__selectImportMethod)


    """
    When the data import method is changed, changing the layout
    """
    def __selectImportMethod(self, item):

        # Select the corresponding widget
        index = self.importMethod_listWidget.currentRow()
        self.importContent_stackedWidget.setCurrentIndex(index)


class ImportPasteMethod(KiangFrame):

     def __init__(self, parent = None):

        # Init
        super(ImportPasteMethod, self).__init__()
        
        """Layout"""
        # This is the layout of the load/paste interface
        self.paste_layout = KiangGridLayout(0)
        
        """Widget"""
        """Main Content Widget"""
        # Message area
        self.pasteMessager_widget = KiangMessager()
        # Textedit
        self.paste_textEdit = KiangTextEdit()
        # Toolbox
        self.paste_toolBox = KiangToolBox()
        # Launch button
        self.pasteRun_pushButton = KiangPushButton(icon = qta.icon("fa.rocket", color = "#ffffff"), 
                                                   text = "ADD TO WAREHOUSE")
        
        """ToolBox Widget"""
        """ToolBox Data Tab"""
        # Layout
        self.pasteData_widget = KiangFrame()
        self.pasteData_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
        """ToolBox Filename"""
        # Filename
        self.pasteDataFilename_label = KiangLabel("Data name")
        self.pasteDataFilename_lineEdit = KiangLineEdit()
        """ToolBox Delimiter"""
        # Delimiter
        self.pasteDataDelimiter_label = KiangLabel("Delimiter")
        # Groupbox for delimiter
        self.pasteDataDelimiter_groupBox =  KiangGroupBox()
        # Groupbox layout
        self.pasteDataDelimiterGroupBox_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
        # Button group for delimiter
        self.pasteDataDelimiter_buttonGroup = KiangButtonGroup()
        # Delimiter: comma, semi-colon, space, tab
        # Each button
        self.pasteDataComma_radioButton = KiangRadioButton(text = "Comma", checked = True)
        self.pasteDataSemiColon_radioButton = KiangRadioButton(text = "Semicolon")
        self.pasteDataSpace_radioButton = KiangRadioButton(text = "Space")
        self.pasteDataTab_radioButton = KiangRadioButton(text = "Tab")
        # Add button to buttonGroup
        self.pasteDataDelimiter_buttonGroup.addButton([self.pasteDataComma_radioButton,
                                                       self.pasteDataSemiColon_radioButton,
                                                       self.pasteDataSpace_radioButton,
                                                       self.pasteDataTab_radioButton])
        # Add button to widget layout
        self.pasteDataDelimiterGroupBox_layout.addWidget([self.pasteDataComma_radioButton, 
                                                          self.pasteDataSemiColon_radioButton,
                                                          self.pasteDataSpace_radioButton, 
                                                          self.pasteDataTab_radioButton])
        # Set layout to button group
        self.pasteDataDelimiter_groupBox.setLayout(self.pasteDataDelimiterGroupBox_layout)
        """ToolBox Statistics"""
        # Statistics
        self.pasteDataStats_label = KiangLabel("Statistics", hidden = True)
        # GroupBox for statistics
        self.pasteDataStats_groupBox = KiangGroupBox(hidden = True)
        # Groupbox layout
        self.pasteDataStatsGroupBox_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
        # Statistics label
        self.pasteDataStatsNRow_label = KiangLabel("")
        self.pasteDataStatsNCol_label = KiangLabel("")
        self.pasteDataStatsMissing_label = KiangLabel("")
        # Add label to layout
        self.pasteDataStatsGroupBox_layout.addWidget([self.pasteDataStatsNRow_label, 
                                                      self.pasteDataStatsNCol_label,
                                                      self.pasteDataStatsMissing_label])
        # Set layout to label group
        self.pasteDataStats_groupBox.setLayout(self.pasteDataStatsGroupBox_layout)
        # Add widgets to layout
        self.pasteData_layout.addWidget([self.pasteDataFilename_label, self.pasteDataFilename_lineEdit,
                                         self.pasteDataDelimiter_label, self.pasteDataDelimiter_groupBox,
                                         self.pasteDataStats_label, self.pasteDataStats_groupBox])
        self.pasteData_layout.addStretch(1)
        # Set layout
        self.pasteData_widget.setLayout(self.pasteData_layout)
        
        
        """ToolBox Row Tab"""
        # Row
        # Layout
        self.pasteRow_widget = KiangFrame()
        self.pasteRow_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
        """Header"""
        # Checkbox for first row as header
        self.pasteRowHeader_label = KiangLabel("Header")
        self.pasteRowHeader_checkBox = KiangCheckBox(text = "First row as header", checked = True)
        """Range"""
        # Range
        self.pasteRowRange_label = KiangLabel("Row Range", hidden = True)
        self.pasteRowRange_widget = KiangFrame(hidden = True)
        # Row range layout
        self.pasteRowRange_layout = KiangGridLayout(0)
        # Row range spinBox for min
        self.pasteRowRangeMin_label =  KiangLabel("Min:")
        self.pasteRowRangeMin_spinBox = KiangSpinBox(min = 1)
        # Row range spinBox for max, at least 2 rows
        self.pasteRowRangeMax_label = KiangLabel("Max:")
        self.pasteRowRangeMax_spinBox = KiangSpinBox(min = 2)
        # Add item to layout
        self.pasteRowRange_layout.addWidget([self.pasteRowRangeMin_label, 
                                             self.pasteRowRangeMin_spinBox,
                                             self.pasteRowRangeMax_label,
                                             self.pasteRowRangeMax_spinBox], 
                                            [[0, 0, 1, 1], [0, 1, 1, 1], 
                                             [1, 0, 1, 1], [1, 1, 1, 1]])
        # Set layout
        self.pasteRowRange_widget.setLayout(self.pasteRowRange_layout)
        # Add widgets to layout
        self.pasteRow_layout.addWidget([self.pasteRowHeader_label, 
                                        self.pasteRowHeader_checkBox,
                                        self.pasteRowRange_label, 
                                        self.pasteRowRange_widget])
        self.pasteRow_layout.addStretch(1)
        # Set layout
        self.pasteRow_widget.setLayout(self.pasteRow_layout)


        """ToolBox Column Tab"""
        # Layout
        self.pasteCol_widget = KiangFrame()
        self.pasteCol_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
        """Index"""
        # Checkbox for first column as index
        self.pasteColIndex_label = KiangLabel("Index")
        self.pasteColIndex_checkBox = KiangCheckBox(text = "First column as index", checked = False)
        """Range"""
        self.pasteColRange_label = KiangLabel("Column Range", hidden = True)
        self.pasteColRange_widget = KiangFrame(hidden = True)
        # Layout
        self.pasteColRange_layout = KiangGridLayout(0)
        # Widgets
        self.pasteColRangeMin_label =  KiangLabel("Min:")
        self.pasteColRangeMin_spinBox = KiangSpinBox(min = 1)
        # Users can select only one variable from the data
        self.pasteColRangeMax_label = KiangLabel("Max:")
        self.pasteColRangeMax_spinBox = KiangSpinBox(min = 1)
        # Add item to layout
        self.pasteColRange_layout.addWidget([self.pasteColRangeMin_label,
                                             self.pasteColRangeMin_spinBox,
                                             self.pasteColRangeMax_label,
                                             self.pasteColRangeMax_spinBox],
                                            [[0, 0, 1, 1], [0, 1, 1, 1],
                                             [1, 0, 1, 1], [1, 1, 1, 1]])
        # Set layout to the widget
        self.pasteColRange_widget.setLayout(self.pasteColRange_layout)
        
        # Add widgets to layout
        self.pasteCol_layout.addWidget([self.pasteColIndex_label, self.pasteColIndex_checkBox,
                                        self.pasteColRange_label, self.pasteCol_widget])
        self.pasteCol_layout.addStretch(1)
        
        # Set layout
        self.pasteCol_widget.setLayout(self.pasteCol_layout)


        """ToolBox Missing Tab"""
        self.pasteMissing_widget = KiangFrame(enabled = False)
        # Layout
        self.pasteMissing_layout = KiangBoxLayout(2, [0, 0, 0, 0], 0)
        """Delete Missing"""
        self.pasteMissingDel_label = KiangLabel("Missing Cells")
        # Groupbox
        self.pasteMissingDel_groupBox = KiangGroupBox("")
        # Layout
        self.pasteMissingDelGroupBox_layout = KiangBoxLayout(2)
        # ButtonGroup
        self.pasteMissingDel_buttonGroup = KiangButtonGroup()
        # Radiobutton
        self.pasteMissingDel_radioButton = KiangRadioButton(text = "Delete")
        self.pasteMissingKeep_radioButton = KiangRadioButton(text = "Keep all", checked = True)
        self.pasteMissingKeepOnly_radioButton = KiangRadioButton(text = "Keep missing only")
        # Add button to buttonGroup
        self.pasteMissingDel_buttonGroup.addButton([self.pasteMissingDel_radioButton,
                                                    self.pasteMissingKeep_radioButton,
                                                    self.pasteMissingKeepOnly_radioButton])
        # Add widget to layout     
        self.pasteMissingDelGroupBox_layout.addWidget([self.pasteMissingDel_radioButton,
                                                       self.pasteMissingKeep_radioButton,
                                                       self.pasteMissingKeepOnly_radioButton])
        # Set layout to groupBox
        self.pasteMissingDel_groupBox.setLayout(self.pasteMissingDelGroupBox_layout)
        
        # Add widget to layout
        self.pasteMissing_layout.addWidget([self.pasteMissingDel_label, 
                                            self.pasteMissingDel_groupBox])
        self.pasteMissing_layout.addStretch(1)
        # Set layout
        self.pasteMissing_widget.setLayout(self.pasteMissing_layout)
          
        # Add item to toolBox
        self.paste_toolBox.addItem([self.pasteData_widget,
                                    self.pasteRow_widget,
                                    self.pasteCol_widget,
                                    self.pasteMissing_widget], 
                                   [qta.icon("fa.heartbeat", color = "#5a5e5a"),
                                    qta.icon("fa.list-ol", color = "#5a5e5a"),
                                    qta.icon("fa.columns", color = "#5a5e5a"),
                                    qta.icon("fa.paw", color = "#5a5e5a")], 
                                   ["DATA", "ROW", "COL", "MISSING"])
        
        
        # Add widget to layout
        self.paste_layout.addWidget([self.pasteMessager_widget,
                                     self.paste_textEdit,
                                     self.paste_toolBox, 
                                     self.pasteRun_pushButton], 
                                    [[0, 0, 1, 6], 
                                     [1, 0, 20, 6],
                                     [0, 6, 20, 1],
                                     [18, 6, 1, 1]])
        # Set layout
        self.setLayout(self.paste_layout)


        """Variable"""
        # Shape
        self.shape = [0, 0]
        # Dict for delimiter
        self.delimiter_dict = {0: ",", 1: ";", 2: " ", 3: "\t"}
        # Default delimiter is comma
        self.delimiter = self.delimiter_dict[0]
        # Filename
        self.filename = ""
        # First row as header
        self.firstRowHeader = True
        # First col as index
        self.firstColIndex = False
        # Count of missing cells
        self.missingCount = 0
        # Missing value
        self.missingDel = False
        # Default keep all
        self.missingDelOption = 1

     
        """Signal"""
        self.paste_textEdit.textChanged.connect(self.getData)
        self.pasteDataComma_radioButton.toggled.connect(self.getDelimiter)
        self.pasteDataSemiColon_radioButton.toggled.connect(self.getDelimiter)
        self.pasteDataSpace.rdioButton.toggled.connect(self.getDelimiter)
        self.pasteDataTab_radioButton.toggled.connect(self.getDelimiter)
        self.pasteRowHeader_checkBox.toggled.connect(self.setHeader)
        self.pasteRowRangeMin_spinBox.valueChanged.connect(self.setRowRangeMinValue)
        self.pasteRowRangeMax_spinBox.valueChanged.connect(self.setRowRangeMaxValue)
        self.pasteColIndex_checkBox.toggled.connect(self.setIndex)
        self.pasteColRangeMin_spinBox.valueChanged.connect(self.setColRangeMinValue)
        self.pasteColRangeMax_spinBox.valueChanged.connect(self.setColRangeMaxValue)
        self.pasteMissingDel_radioButton.toggled.connect(self.getMissing)
        self.pasteMissingKeep_radioButton.toggled.connect(self.getMissing)
        self.pasteMissingKeepOnly_radioButton.toggled.connect(self.getMissing)
        # self.pasteDataFilename_lineEdit.textChanged.connect(self.getFilename)


     # Obtain the delimiter from the interface
     def getDelimiter(self, toggledOn):

          # If toggled off signal, return
          if not toggledOn:

               return
          
          checked_id = self.pasteDataDelimiter_buttonGroup.checkedId()
          self.delimiter = self.delimiter_dict[checked_id]
          # Everytime checked a new radio button, read the data again
          self.getData()

     # Obtain data
     def getData(self):

          # If not space delimiter, strip all the space
          if self.delimiter != " ":
               
               text = self.paste_textEdit.toPlainText().replace(" ", "")

          else:

               text = self.paste_textEdit.toPlainText()

          # If this is the first line, skipped
          if "\n" not in text:

               return
          
          buffer = StringIO(text)
          header = 0 if self.firstRowHeader else None
          row_index = 0 if self.firstColIndex else False
          try:

                # Index_col is set to false as default
                reader = pd.io.parsers.read_csv(buffer, delimiter = self.delimiter, header = header, index_col = row_index)
                msg = ""
                self.pasteMessager_widget(msg, "VoidMessager")

          except pd.parser.CParserError:

               msg = "Cannot parse the data !"
               self.pasteMessager_widget.msg(msg, "ErrorMessager")
               reader = pd.DataFrame()

          except IndexError:

               msg = "Index out of range !"
               self.pasteMessager_widget.msg(msg, "ErrorMessager")
               reader = pd.DataFrame()

          # Get statistics
          self.shape = reader.shape
          self.missingCount = reader.isnull().values.ravel().sum()
          if self.shape[0] > 1:

                self.pasteDataStatsNrow_label.setText("Rows:%s"% (self.shape[0]))
                self.pasteDataStatsNcol_label.setText("Cols:%s"% (self.shape[1]))
                self.pasteDataStatsMissing_label.setText("Missing cells: %s"% (self.missingCount))
                self.showStats(True)
                self.showRowRange(True)
                self.showColRange(True)
                self.showMissing(self.missingCount > 0)

          else:

               self.showStats(False)
               self.showRowRange(False)
               self.showColRange(False)
               self.showMissing(False)
                    
     def getFilename(self):

          # Get filename and replace the space with underscore
          filename = self.pasteDataFilename_lineEdit.text().replace(" ", "_")

     def getMissing(self):

          # Get missing
          self.missingDelOption = self.pasteMissingDel_buttonGroup.checkedId()
          

     # Set the range for row min
     def setColRangeMinValue(self):

          # Get values 
          minValue = int(self.pasteColRangeMin_spinBox.value())
          maxValue = int(self.pasteColRangeMax_spinBox.value())
          if maxValue < minValue:

               self.pasteColRangeMax_spinBox.setValue(minValue)
               
     # Set the range for row max
     def setColRangeMaxValue(self):

          # Get values 
          minValue = int(self.pasteColRangeMin_spinBox.value())
          maxValue = int(self.pasteColRangeMax_spinBox.value())
          if maxValue < minValue:

               self.pasteColRangeMin_spinBox.setValue(maxValue)
               
     # Set header
     def setHeader(self, toggledOn):

          self.firstRowHeader = True if toggledOn == True else False
          self.getData()

     # Index
     def setIndex(self, toggledOn):

          self.firstColIndex = True if toggledOn == True else False
          self.getData()
          
     # Set the range for row min
     def setRowRangeMinValue(self):

          # Get values 
          minValue = int(self.pasteRowRangeMin_spinBox.value())
          maxValue = int(self.pasteRowRangeMax_spinBox.value())
          if maxValue <= minValue:

               self.pasteRowRangeMax_spinBox.setValue(minValue + 1)
               
     # Set the range for row max
     def setRowRangeMaxValue(self):

          # Get values 
          minValue = int(self.pasteRowRangeMin_spinBox.value())
          maxValue = int(self.pasteRowRangeMax_spinBox.value())
          if maxValue <= minValue:

               self.pasteRowRangeMin_spinBox.setValue(maxValue - 1)

     # Functions to show the column range
     def showColRange(self, showFlag):

          self.pasteColRange_label.setVisible(showFlag)
          self.pasteColRange_widget.setVisible(showFlag)
          maxAllowed = 1 if self.shape[1] == 1 else self.shape[1]
          self.pasteColRangeMin_spinBox.setMaximum(maxAllowed)
          self.pasteColRangeMax_spinBox.setMaximum(maxAllowed)
          self.pasteColRangeMin_spinBox.setValue(1)
          self.pasteColRangeMax_spinBox.setValue(maxAllowed)

     # Funcions to show the missing data tab
     def showMissing(self, showFlag):

          self.pasteMissing_widget.setEnabled(showFlag)
          
     # Functions to show the statistics
     def showStats(self, showFlag):

          self.pasteDataStats_label.setVisible(showFlag)
          self.pasteDataStats_groupBox.setVisible(showFlag)


     # Functions to show the row range
     def showRowRange(self, showFlag):

          self.pasteRowRange_label.setVisible(showFlag)
          self.pasteRowRange_widget.setVisible(showFlag)
          maxAllowed = 2 if self.shape[0] <= 2 else self.shape[0]
          self.pasteRowRangeMin_spinBox.setMaximum(maxAllowed - 1)
          self.pasteRowRangeMax_spinBox.setMaximum(maxAllowed)
          self.pasteRowRangeMin_spinBox.setValue(1)
          self.pasteRowRangeMax_spinBox.setValue(maxAllowed)
               
               

class ImportDragMethod(QtWidgets.QFrame):

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
