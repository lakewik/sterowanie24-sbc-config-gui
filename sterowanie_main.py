# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sterowanie_config.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1015, 676)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 10, 341, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 40, 981, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 561, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 301, 32))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 541, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(460, 40, 16, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 40, 81, 32))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 371, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 80, 71, 32))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(470, 80, 71, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 181, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 171, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 120, 341, 32))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 160, 351, 32))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 200, 341, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(590, 60, 411, 241))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 391, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.groupBox_2)
        self.line_4.setGeometry(QtCore.QRect(189, 40, 31, 191))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.groupBox_2)
        self.line_5.setGeometry(QtCore.QRect(10, 120, 391, 31))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(80, 40, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 141, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(270, 40, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(220, 100, 161, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(80, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 200, 171, 31))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(270, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(220, 200, 181, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 310, 561, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.line_6 = QtGui.QFrame(self.groupBox_3)
        self.line_6.setGeometry(QtCore.QRect(10, 20, 541, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 221, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(240, 40, 311, 32))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(590, 310, 411, 91))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.line_7 = QtGui.QFrame(self.groupBox_4)
        self.line_7.setGeometry(QtCore.QRect(10, 20, 391, 20))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(20, 40, 371, 31))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 410, 981, 211))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.line_8 = QtGui.QFrame(self.groupBox_5)
        self.line_8.setGeometry(QtCore.QRect(10, 20, 961, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.tableView = QtGui.QTableView(self.groupBox_5)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 961, 161))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(20, 630, 151, 34))
        self.toolButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(850, 630, 151, 34))
        self.toolButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(180, 630, 151, 34))
        self.toolButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Konfiguracja sterowania online</span></p></body></html>", None))
        self.groupBox.setTitle(_translate("Dialog", "Połączenie", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Adres serwera:</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">:</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Czas odstępu pomiędzy sprawdzeniami stanu:</span></p></body></html>", None))
        self.lineEdit_3.setText(_translate("Dialog", "0.5", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">sekund</span></p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Identyfikator modułu:</span></p></body></html>", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Token autoryzacyjny:</span></p></body></html>", None))
        self.checkBox.setText(_translate("Dialog", "Przekazuj do serwera aktualny uptime", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Statystyki", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt;\">12</span></p></body></html>", None))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wszystkich GPIO</span></p></body></html>", None))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt;\">12</span></p></body></html>", None))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Nieużywanych GPIO</span></p></body></html>", None))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt;\">12</span></p></body></html>", None))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Kanałów sterujących</span></p></body></html>", None))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt;\">12</span></p></body></html>", None))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Użytkowników online</span></p></body></html>", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Przełączanie", None))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Stan wysoki odpowiada za:</span></p></body></html>", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Stan daemona", None))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wyłączony</span></p></body></html>", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Przypisywanie GPIO", None))
        self.toolButton.setText(_translate("Dialog", "Uruchom daemona", None))
        self.toolButton_2.setText(_translate("Dialog", "Zapisz ustawienia", None))
        self.toolButton_3.setText(_translate("Dialog", "Zrestartuj daemona", None))

