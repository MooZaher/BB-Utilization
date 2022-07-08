# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_BB.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 501, 41))
        self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.load_ran1 = QtWidgets.QPushButton(self.centralwidget)
        self.load_ran1.setGeometry(QtCore.QRect(10, 62, 111, 41))
        self.load_ran1.setObjectName("load_ran1")
        self.load_ran_2 = QtWidgets.QPushButton(self.centralwidget)
        self.load_ran_2.setGeometry(QtCore.QRect(10, 110, 111, 41))
        self.load_ran_2.setObjectName("load_ran_2")
        self.progressBar_ran1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_ran1.setGeometry(QtCore.QRect(140, 70, 181, 21))
        self.progressBar_ran1.setProperty("value", 24)
        self.progressBar_ran1.setObjectName("progressBar_ran1")
        self.progressBar_ran2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_ran2.setGeometry(QtCore.QRect(140, 120, 181, 20))
        self.progressBar_ran2.setProperty("value", 24)
        self.progressBar_ran2.setObjectName("progressBar_ran2")
        self.text_ran1_load = QtWidgets.QLabel(self.centralwidget)
        self.text_ran1_load.setGeometry(QtCore.QRect(330, 70, 171, 21))
        self.text_ran1_load.setObjectName("text_ran1_load")
        self.text_ran2_load = QtWidgets.QLabel(self.centralwidget)
        self.text_ran2_load.setGeometry(QtCore.QRect(330, 120, 171, 21))
        self.text_ran2_load.setObjectName("text_ran2_load")
        self.processing_files = QtWidgets.QLabel(self.centralwidget)
        self.processing_files.setGeometry(QtCore.QRect(20, 220, 161, 301))
        self.processing_files.setObjectName("processing_files")
        self.progressBar_process = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_process.setGeometry(QtCore.QRect(80, 542, 421, 21))
        self.progressBar_process.setProperty("value", 24)
        self.progressBar_process.setObjectName("progressBar_process")
        self.status_text = QtWidgets.QLabel(self.centralwidget)
        self.status_text.setGeometry(QtCore.QRect(10, 540, 121, 21))
        self.status_text.setObjectName("status_text")
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setGeometry(QtCore.QRect(80, 572, 111, 31))
        self.open_btn.setObjectName("open_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(310, 570, 111, 31))
        self.exit_btn.setObjectName("exit_btn")
        self.below_60 = QtWidgets.QLabel(self.centralwidget)
        self.below_60.setGeometry(QtCore.QRect(260, 300, 51, 41))
        self.below_60.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.below_60.setText("")
        self.below_60.setAlignment(QtCore.Qt.AlignCenter)
        self.below_60.setObjectName("below_60")
        self.no_severity = QtWidgets.QLabel(self.centralwidget)
        self.no_severity.setGeometry(QtCore.QRect(390, 300, 51, 41))
        self.no_severity.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.no_severity.setText("")
        self.no_severity.setAlignment(QtCore.Qt.AlignCenter)
        self.no_severity.setObjectName("no_severity")
        self.between_60_90 = QtWidgets.QLabel(self.centralwidget)
        self.between_60_90.setGeometry(QtCore.QRect(260, 390, 51, 41))
        self.between_60_90.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.between_60_90.setText("")
        self.between_60_90.setAlignment(QtCore.Qt.AlignCenter)
        self.between_60_90.setObjectName("between_60_90")
        self.weak_moderate = QtWidgets.QLabel(self.centralwidget)
        self.weak_moderate.setGeometry(QtCore.QRect(390, 390, 51, 41))
        self.weak_moderate.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.weak_moderate.setText("")
        self.weak_moderate.setAlignment(QtCore.Qt.AlignCenter)
        self.weak_moderate.setObjectName("weak_moderate")
        self.above_90 = QtWidgets.QLabel(self.centralwidget)
        self.above_90.setGeometry(QtCore.QRect(260, 480, 51, 41))
        self.above_90.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.above_90.setText("")
        self.above_90.setAlignment(QtCore.Qt.AlignCenter)
        self.above_90.setObjectName("above_90")
        self.high_veryhigh = QtWidgets.QLabel(self.centralwidget)
        self.high_veryhigh.setGeometry(QtCore.QRect(390, 480, 51, 41))
        self.high_veryhigh.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.high_veryhigh.setText("")
        self.high_veryhigh.setAlignment(QtCore.Qt.AlignCenter)
        self.high_veryhigh.setObjectName("high_veryhigh")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(236, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 270, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 270, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 360, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 360, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 450, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 450, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.execute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.execute_btn.setGeometry(QtCore.QRect(114, 165, 241, 41))
        self.execute_btn.setObjectName("execute_btn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 165, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">Welcome to BB Utilization tool</span></p></body></html>"))
        self.load_ran1.setText(_translate("MainWindow", "Load RAN 1"))
        self.load_ran_2.setText(_translate("MainWindow", "Load RAN 2"))
        self.text_ran1_load.setText(_translate("MainWindow", "RAN1 Loaded Successfully :)"))
        self.text_ran2_load.setText(_translate("MainWindow", "RAN2 Loaded Successfully :)"))
        self.processing_files.setText(_translate("MainWindow", "Processing Files ...."))
        self.status_text.setText(_translate("MainWindow", "Status Bar"))
        self.open_btn.setText(_translate("MainWindow", "Open Output"))
        self.exit_btn.setText(_translate("MainWindow", "Exit App"))
        self.label.setText(_translate("MainWindow", "KPIs Highlights"))
        self.label_2.setText(_translate("MainWindow", "Below 60%"))
        self.label_3.setText(_translate("MainWindow", "No Severity"))
        self.label_4.setText(_translate("MainWindow", "Between 60%90%"))
        self.label_5.setText(_translate("MainWindow", "Weak/Moderate"))
        self.label_6.setText(_translate("MainWindow", "Above 90%"))
        self.label_7.setText(_translate("MainWindow", "High/Very High"))
        self.execute_btn.setText(_translate("MainWindow", "Execute"))