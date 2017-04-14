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