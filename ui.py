# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from main import login, loadClasses, loadBaliks, train_balik, work
import time

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickForm = QtWidgets.QLineEdit(self.centralwidget)
        self.nickForm.setGeometry(QtCore.QRect(20, 50, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nickForm.setFont(font)
        self.nickForm.setText("")
        self.nickForm.setObjectName("nickForm")
        self.nickLabel = QtWidgets.QLabel(self.centralwidget)
        self.nickLabel.setGeometry(QtCore.QRect(20, 15, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nickLabel.setFont(font)
        self.nickLabel.setObjectName("nickLabel")
        self.passwordForm = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordForm.setGeometry(QtCore.QRect(20, 110, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordForm.setFont(font)
        self.passwordForm.setText("")
        self.passwordForm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordForm.setObjectName("passwordForm")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 75, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.chooseClassBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseClassBox.setGeometry(QtCore.QRect(20, 220, 201, 22))
        self.chooseClassBox.setObjectName("chooseClassBox")
        self.chooseClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseClassLabel.setGeometry(QtCore.QRect(20, 180, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chooseClassLabel.setFont(font)
        self.chooseClassLabel.setObjectName("chooseClassLabel")
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.chooseButton.setObjectName("chooseButton")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(20, 150, 75, 23))
        self.loginButton.setCheckable(False)
        self.loginButton.setObjectName("loginButton")
        self.trainButton = QtWidgets.QRadioButton(self.centralwidget)
        self.trainButton.setGeometry(QtCore.QRect(30, 310, 82, 17))
        self.trainButton.setObjectName("trainButton")
        self.workButton = QtWidgets.QRadioButton(self.centralwidget)
        self.workButton.setGeometry(QtCore.QRect(130, 310, 82, 17))
        self.workButton.setObjectName("workButton")
        self.trainPercentButton = QtWidgets.QRadioButton(self.centralwidget)
        self.trainPercentButton.setGeometry(QtCore.QRect(89, 330, 82, 17))
        self.trainPercentButton.setObjectName("trainPercentButton")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(70, 350, 75, 23))
        self.goButton.setObjectName("goButton")
        self.numOfWords = QtWidgets.QSpinBox(self.centralwidget)
        self.numOfWords.setObjectName("numOfWords")
        self.numOfWords.setGeometry(QtCore.QRect(200, 260, 42, 22))
        self.numOfWords.setMinimum(1)
        self.numOfWordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numOfWordsLabel.setObjectName("numOfWordsLabel")
        self.numOfWordsLabel.setGeometry(QtCore.QRect(90, 260, 101, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loggedIn = False
        self.choosingClasses = False
        self.loginButton.clicked.connect(lambda:self.WBlogin())
        self.chooseButton.clicked.connect(lambda:self.choose())
        self.goButton.clicked.connect(lambda:self.doIt())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wocabee Bot"))
        self.nickLabel.setText(_translate("MainWindow", "Name"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.chooseClassLabel.setText(_translate("MainWindow", "Choose class"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.trainButton.setText(_translate("MainWindow", "Train"))
        self.trainPercentButton.setText(_translate("MainWindow", "Train %"))
        self.workButton.setText(_translate("MainWindow", "Work"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.chooseButton.setText(_translate("MainWindow","Choose"))
        self.numOfWordsLabel.setText(_translate("MainWindow", u"How many words", None))

    def WBlogin(self):
        try:
            login(self.nickForm.text(), self.passwordForm.text())
        except:
            pass
        time.sleep(1)
        self.classes = loadClasses()
        self.chooseClassBox.addItems([i.text for i in self.classes])
        self.loggedIn = True

    def choose(self):
        if self.loggedIn:
            for c in self.classes:
                if c.text == self.chooseClassBox.currentText():
                    self.classes[self.classes.index(c)].find_element_by_tag_name("button").click()
                    self.choosingBaliks = True
                    self.baliks = loadBaliks()
                    self.chooseClassBox.clear()
                    self.chooseClassBox.addItems([i.find_elements_by_tag_name('td')[0].text for i in self.baliks])
                    self.chooseClassLabel.setText("Choose balík")

    def doIt(self):
        if self.loggedIn and self.choosingBaliks:
            if self.trainButton.isChecked():
                train_balik(self.baliks, self.chooseClassBox.currentIndex(), f"{self.chooseClassBox.currentText()}.txt")
            elif self.workButton.isChecked():
                work(self.baliks, self.chooseClassBox.currentIndex(), f"{self.chooseClassBox.currentText()}.txt", self.numOfWords.value())




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
