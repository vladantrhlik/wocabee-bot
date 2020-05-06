# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import time
from main import login, train_balik, work, work_percent, loadBaliks, loadClasses, chooseBrowser

from PyQt5 import QtCore, QtGui, QtWidgets

import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 210)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickForm = QtWidgets.QLineEdit(self.centralwidget)
        self.nickForm.setGeometry(QtCore.QRect(20, 45, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nickForm.setFont(font)
        self.nickForm.setText("")
        self.nickForm.setObjectName("nickForm")
        self.nickLabel = QtWidgets.QLabel(self.centralwidget)
        self.nickLabel.setGeometry(QtCore.QRect(20, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nickLabel.setFont(font)
        self.nickLabel.setObjectName("nickLabel")
        self.passwordForm = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordForm.setGeometry(QtCore.QRect(20, 105, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordForm.setFont(font)
        self.passwordForm.setText("")
        self.passwordForm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordForm.setObjectName("passwordForm")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.chooseClassBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseClassBox.setGeometry(QtCore.QRect(20, 50, 201, 22))
        self.chooseClassBox.setObjectName("chooseClassBox")
        self.chooseClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseClassLabel.setGeometry(QtCore.QRect(20, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chooseClassLabel.setFont(font)
        self.chooseClassLabel.setObjectName("chooseClassLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(20, 145, 75, 23))
        self.loginButton.setCheckable(False)
        self.loginButton.setObjectName("loginButton")
        self.trainButton = QtWidgets.QRadioButton(self.centralwidget)
        self.trainButton.setGeometry(QtCore.QRect(30, 90, 51, 17))
        self.trainButton.setObjectName("trainButton")
        self.workButton = QtWidgets.QRadioButton(self.centralwidget)
        self.workButton.setGeometry(QtCore.QRect(100, 90, 51, 17))
        self.workButton.setObjectName("workButton")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(70, 160, 75, 23))
        self.goButton.setObjectName("goButton")
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.chooseButton.setObjectName("chooseButton")
        self.numOfWords = QtWidgets.QSpinBox(self.centralwidget)
        self.numOfWords.setGeometry(QtCore.QRect(200, 130, 42, 22))
        self.numOfWords.setMinimum(1)
        self.numOfWords.setMaximum(10000)
        self.numOfWords.setObjectName("numOfWords")
        self.numOfWordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numOfWordsLabel.setGeometry(QtCore.QRect(90, 130, 101, 20))
        self.numOfWordsLabel.setObjectName("numOfWordsLabel")
        self.chooseBrowserButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseBrowserButton.setGeometry(QtCore.QRect(160, 30, 91, 23))
        self.chooseBrowserButton.setObjectName("chooseBrowserButton")
        self.chooseBrowserBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseBrowserBox.setGeometry(QtCore.QRect(20, 30, 131, 22))
        self.chooseBrowserBox.setObjectName("chooseBrowserBox")
        self.workPercentButton = QtWidgets.QRadioButton(self.centralwidget)
        self.workPercentButton.setGeometry(QtCore.QRect(160, 90, 71, 17))
        self.workPercentButton.setObjectName("workPercentButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.chooseBrowserButton.clicked.connect(lambda:self.WBchooseBrowser())
        self.workButton.toggled.connect(lambda:self.toggleNumOfWords())

        self.loggedIn = False
        self.choosingClasses = False
        self.loginButton.clicked.connect(lambda:self.WBlogin())
        self.chooseButton.clicked.connect(lambda:self.choose())
        self.goButton.clicked.connect(lambda:self.doIt())
        self.chooseBrowserBox.addItems(["Chrome","Firefox","Opera","IE", "Edge","Safari"])

        for i in [self.nickLabel, self.nickForm, self.passwordLabel, self.passwordForm, self.loginButton]:
            i.setVisible(False)
        for i in [self.chooseClassLabel, self.chooseClassBox, self.chooseButton]:
            i.setVisible(False)
        for i in [self.workButton, self.trainButton, self.workPercentButton, self.goButton, self.numOfWordsLabel, self.numOfWords]:
            i.setVisible(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wocabee Bot"))
        self.nickLabel.setText(_translate("MainWindow", "Name"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.chooseClassLabel.setText(_translate("MainWindow", "Chose class"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.trainButton.setText(_translate("MainWindow", "Train"))
        self.workButton.setText(_translate("MainWindow", "Work"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.chooseButton.setText(_translate("MainWindow", "Choose"))
        self.numOfWordsLabel.setText(_translate("MainWindow", "How many words"))
        self.chooseBrowserButton.setText(_translate("MainWindow", "Choose browser"))
        self.workPercentButton.setText(_translate("MainWindow", "Work %"))

    def WBchooseBrowser(self):
        chooseBrowser(self.chooseBrowserBox.currentText())
        for i in [self.chooseBrowserBox, self.chooseBrowserButton]:
            i.setVisible(False)
        for i in [self.nickLabel, self.nickForm, self.passwordLabel, self.passwordForm, self.loginButton]:
            i.setVisible(True)

    def WBlogin(self):
        try:
            login(self.nickForm.text(), self.passwordForm.text())
            self.loggedIn = True
            for i in [self.nickLabel, self.nickForm, self.passwordLabel, self.passwordForm, self.loginButton]:
                i.setVisible(False)
            for i in [self.chooseClassLabel, self.chooseClassBox, self.chooseButton]:
                i.setVisible(True)
        except:
            pass
        time.sleep(1)
        self.classes = loadClasses()
        self.chooseClassBox.addItems([i.text for i in self.classes])


    def choose(self):
        if self.loggedIn:
            self.classes[self.chooseClassBox.currentIndex()].find_element_by_tag_name("button").click()
            self.choosingBaliks = True
            self.baliks = loadBaliks()
            self.chooseClassBox.clear()
            self.chooseClassBox.addItems([i.find_elements_by_tag_name('td')[0].text for i in self.baliks])
            self.chooseClassLabel.setText("Choose balík")
            self.chooseButton.setVisible(False)
            for i in [self.workButton, self.trainButton, self.workPercentButton, self.goButton]:
                i.setVisible(True)

    def doIt(self):
        if self.loggedIn and self.choosingBaliks:
            if self.trainButton.isChecked():
                train_balik(self.baliks, self.chooseClassBox.currentIndex(), f"{self.chooseClassBox.currentText()}.txt")
            elif self.workButton.isChecked():
                work(self.baliks, self.chooseClassBox.currentIndex(), f"{self.chooseClassBox.currentText()}.txt", self.numOfWords.value())
            elif self.workPercentButton.isChecked():
                work_percent(self.baliks, self.chooseClassBox.currentIndex, f"{self.chooseClassBox.currentText()}.txt")

    def toggleNumOfWords(self):
        if self.workButton.isChecked():
            for i in [self.numOfWords, self.numOfWordsLabel]:
                i.setVisible(True)
        else:
            for i in [self.numOfWords, self.numOfWordsLabel]:
                i.setVisible(False)

if __name__ == "__main__":
    blockPrint()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
