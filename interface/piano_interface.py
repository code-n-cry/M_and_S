# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1428, 761)
        Form.setStyleSheet("background-color: rgb(255, 237, 206);\n"
"QLabel {color: black;};\n"
"QMessageBox {color:black};")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 51, 401))
        self.pushButton.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.keyboard = QtWidgets.QButtonGroup(Form)
        self.keyboard.setObjectName("keyboard")
        self.keyboard.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 10, 51, 401))
        self.pushButton_2.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.keyboard.addButton(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 60, 51, 401))
        self.pushButton_3.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.keyboard.addButton(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 10, 51, 401))
        self.pushButton_4.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.keyboard.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 60, 51, 401))
        self.pushButton_5.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.keyboard.addButton(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 60, 51, 401))
        self.pushButton_7.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.keyboard.addButton(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 10, 51, 391))
        self.pushButton_6.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.keyboard.addButton(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 60, 51, 401))
        self.pushButton_8.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.keyboard.addButton(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 10, 51, 391))
        self.pushButton_9.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.keyboard.addButton(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(470, 60, 51, 401))
        self.pushButton_10.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.keyboard.addButton(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(520, 10, 51, 391))
        self.pushButton_11.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.keyboard.addButton(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(570, 60, 51, 401))
        self.pushButton_12.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.keyboard.addButton(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 60, 51, 401))
        self.pushButton_13.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.keyboard.addButton(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(690, 10, 51, 391))
        self.pushButton_14.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.keyboard.addButton(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(740, 60, 51, 401))
        self.pushButton_15.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.keyboard.addButton(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(790, 10, 51, 391))
        self.pushButton_16.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.keyboard.addButton(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(840, 60, 51, 401))
        self.pushButton_17.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.keyboard.addButton(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(910, 60, 51, 401))
        self.pushButton_18.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.keyboard.addButton(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(960, 10, 51, 391))
        self.pushButton_19.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.keyboard.addButton(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(1010, 60, 51, 401))
        self.pushButton_20.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.keyboard.addButton(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(1060, 10, 51, 391))
        self.pushButton_21.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.keyboard.addButton(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setGeometry(QtCore.QRect(1110, 60, 51, 401))
        self.pushButton_22.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.keyboard.addButton(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setGeometry(QtCore.QRect(1160, 0, 51, 391))
        self.pushButton_23.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.keyboard.addButton(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setGeometry(QtCore.QRect(1210, 60, 51, 401))
        self.pushButton_24.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.keyboard.addButton(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(Form)
        self.pushButton_25.setGeometry(QtCore.QRect(1270, 60, 51, 401))
        self.pushButton_25.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 3px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_25.setObjectName("pushButton_25")
        self.keyboard.addButton(self.pushButton_25)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 520, 161, 31))
        self.label.setStyleSheet("color: black")
        self.label.setObjectName("label")
        self.volumeSlider = QtWidgets.QSlider(Form)
        self.volumeSlider.setGeometry(QtCore.QRect(260, 530, 571, 16))
        self.volumeSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid #565a5e;\n"
"    height: 12px;\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #565a5e;\n"
"    width: 24px;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}")
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeLevel = QtWidgets.QLabel(Form)
        self.volumeLevel.setGeometry(QtCore.QRect(860, 530, 101, 21))
        self.volumeLevel.setStyleSheet("color: black")
        self.volumeLevel.setObjectName("volumeLevel")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1020, 520, 121, 31))
        self.label_5.setStyleSheet("color: black")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(1190, 520, 131, 31))
        self.comboBox.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 7px;\n"
"QComboBox::hover{\n"
"    border: 3px solid yellow;\n"
"    color: white;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 600, 191, 21))
        self.label_3.setStyleSheet("color: black")
        self.label_3.setObjectName("label_3")
        self.durationlSlider = QtWidgets.QSlider(Form)
        self.durationlSlider.setGeometry(QtCore.QRect(260, 600, 571, 16))
        self.durationlSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 3px solid #565a5e;\n"
"    height: 12px;\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #565a5e;\n"
"    width: 24px;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}")
        self.durationlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.durationlSlider.setObjectName("durationlSlider")
        self.durationLevel = QtWidgets.QLabel(Form)
        self.durationLevel.setGeometry(QtCore.QRect(860, 600, 101, 21))
        self.durationLevel.setStyleSheet("color:black")
        self.durationLevel.setObjectName("durationLevel")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(1010, 570, 321, 31))
        self.addButton.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 9px;\n"
"background-color: yellow;\n"
"color: black;")
        self.addButton.setObjectName("addButton")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(1010, 680, 331, 31))
        self.playButton.setStyleSheet("border: 2px solid gray;\n"
"border-radius: 9px;\n"
"background-color: yellow;\n"
"color: black;")
        self.playButton.setObjectName("playButton")
        self.selected = QtWidgets.QLabel(Form)
        self.selected.setGeometry(QtCore.QRect(20, 680, 801, 31))
        self.selected.setStyleSheet("color: black\n"
"")
        self.selected.setObjectName("selected")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "??????????????"))
        self.pushButton.setText(_translate("Form", "C1"))
        self.pushButton_2.setText(_translate("Form", "C#1"))
        self.pushButton_3.setText(_translate("Form", "D1"))
        self.pushButton_4.setText(_translate("Form", "D#1"))
        self.pushButton_5.setText(_translate("Form", "E1"))
        self.pushButton_7.setText(_translate("Form", "F1"))
        self.pushButton_6.setText(_translate("Form", "F#1"))
        self.pushButton_8.setText(_translate("Form", "G1"))
        self.pushButton_9.setText(_translate("Form", "G#1"))
        self.pushButton_10.setText(_translate("Form", "A1"))
        self.pushButton_11.setText(_translate("Form", "A#1"))
        self.pushButton_12.setText(_translate("Form", "B1"))
        self.pushButton_13.setText(_translate("Form", "C2"))
        self.pushButton_14.setText(_translate("Form", "C#2"))
        self.pushButton_15.setText(_translate("Form", "D2"))
        self.pushButton_16.setText(_translate("Form", "D#2"))
        self.pushButton_17.setText(_translate("Form", "E2"))
        self.pushButton_18.setText(_translate("Form", "F2"))
        self.pushButton_19.setText(_translate("Form", "F#2"))
        self.pushButton_20.setText(_translate("Form", "G2"))
        self.pushButton_21.setText(_translate("Form", "G#2"))
        self.pushButton_22.setText(_translate("Form", "A2"))
        self.pushButton_23.setText(_translate("Form", "A#2"))
        self.pushButton_24.setText(_translate("Form", "B2"))
        self.pushButton_25.setText(_translate("Form", "C3"))
        self.label.setText(_translate("Form", "??????????????????:"))
        self.volumeLevel.setText(_translate("Form", "1"))
        self.label_5.setText(_translate("Form", "????????????:"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.comboBox.setItemText(2, _translate("Form", "3"))
        self.comboBox.setItemText(3, _translate("Form", "4"))
        self.comboBox.setItemText(4, _translate("Form", "5"))
        self.comboBox.setItemText(5, _translate("Form", "6"))
        self.comboBox.setItemText(6, _translate("Form", "7"))
        self.comboBox.setItemText(7, _translate("Form", "8"))
        self.label_3.setText(_translate("Form", "??????????????????????????:"))
        self.durationLevel.setText(_translate("Form", "1"))
        self.addButton.setText(_translate("Form", "???????????????? ?? ??????????????"))
        self.playButton.setText(_translate("Form", "???????????????????? ????????"))
        self.selected.setText(_translate("Form", "?????????????????? ????????, ????????????????????????, ??????????????????"))
