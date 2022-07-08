import datetime
from time import sleep
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import Helpers
from ui_BB import Ui_MainWindow

current_date = datetime.date.today().strftime("%Y%m%d")


class BBtool(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(BBtool, self).__init__(parent)
        self.setupUi(self)
        Helpers.gui_initialization(self)
        self.exit_btn.clicked.connect(self.close)

        self.load_ran1.clicked.connect(self.load_RAN_1_click)
        self.load_ran_2.clicked.connect(self.load_RAN_2_click)
        self.execute_btn.clicked.connect(lambda: Helpers.prepare_sheets(self, self.ran1wb, self.ran2wb))

    def load_RAN_1_click(self):
        fileName = QFileDialog.getOpenFileName(filter="Excel (*.xlsx *.xls *.csv)")
        if fileName[0] == "":
            Helpers.messageBox(self, "Caution!", "No File Uploaded")
        else:
            path = fileName[0]
            self.progressBar_ran1.show()
            self.progressBar_ran1.setValue(4)
            self.ran1wb = Helpers.load_files(path)
            Helpers.progressBar(self, self.progressBar_ran1)
            self.text_ran1_load.show()

    def load_RAN_2_click(self):
        fileName = QFileDialog.getOpenFileName(filter="Excel (*.xlsx *.xls *.csv)")
        if fileName[0] == "":
            Helpers.messageBox(self, "Caution!", "No File Uploaded")
        else:
            path = fileName[0]
            self.progressBar_ran2.show()
            self.progressBar_ran2.setValue(4)
            self.ran2wb = Helpers.load_files(path)
            Helpers.progressBar(self, self.progressBar_ran2)
            self.text_ran2_load.show()

#####################
#        MAIN       #
#####################
app = QtWidgets.QApplication(sys.argv)
bbUtilization = BBtool()
bbUtilization.show()
sys.exit(app.exec_())
