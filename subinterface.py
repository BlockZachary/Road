# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subinterface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1330, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(105, 99, 1120, 691))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.background_label.setFont(font)
        self.background_label.setAutoFillBackground(False)
        self.background_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.background_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_label.setMidLineWidth(0)
        self.background_label.setText("")
        self.background_label.setTextFormat(QtCore.Qt.AutoText)
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")
        self.label_return = QtWidgets.QLabel(self.centralwidget)
        self.label_return.setGeometry(QtCore.QRect(140, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_return.setFont(font)
        self.label_return.setAlignment(QtCore.Qt.AlignCenter)
        self.label_return.setObjectName("label_return")
        self.button_return = QtWidgets.QPushButton(self.centralwidget)
        self.button_return.setGeometry(QtCore.QRect(140, 130, 61, 61))
        self.button_return.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    border-image: url(:/icon/ui_image/返回箭头.png);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(179, 179, 179);\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_return.setText("")
        self.button_return.setObjectName("button_return")
        self.label_navigationimage = QtWidgets.QLabel(self.centralwidget)
        self.label_navigationimage.setGeometry(QtCore.QRect(140, 310, 611, 431))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_navigationimage.setFont(font)
        self.label_navigationimage.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius: 10px;")
        self.label_navigationimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_navigationimage.setObjectName("label_navigationimage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 160, 731, 81))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 B")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_task = QtWidgets.QLabel(self.centralwidget)
        self.label_task.setGeometry(QtCore.QRect(800, 350, 60, 60))
        self.label_task.setStyleSheet("border-image: url(:/icon/ui_image/目标.svg);")
        self.label_task.setText("")
        self.label_task.setObjectName("label_task")
        self.lineEdit_targettask = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_targettask.setGeometry(QtCore.QRect(860, 349, 311, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_targettask.setFont(font)
        self.lineEdit_targettask.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_targettask.setObjectName("lineEdit_targettask")
        self.label_local = QtWidgets.QLabel(self.centralwidget)
        self.label_local.setGeometry(QtCore.QRect(800, 461, 60, 60))
        self.label_local.setStyleSheet("border-image: url(:/icon/ui_image/当前位置.png);")
        self.label_local.setText("")
        self.label_local.setObjectName("label_local")
        self.lineEdit_currentlocal = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_currentlocal.setGeometry(QtCore.QRect(860, 460, 201, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_currentlocal.setFont(font)
        self.lineEdit_currentlocal.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_currentlocal.setObjectName("lineEdit_currentlocal")
        self.label_routeline = QtWidgets.QLabel(self.centralwidget)
        self.label_routeline.setGeometry(QtCore.QRect(800, 571, 60, 60))
        self.label_routeline.setStyleSheet("border-image: url(:/icon/ui_image/巡视路线.png);")
        self.label_routeline.setText("")
        self.label_routeline.setObjectName("label_routeline")
        self.lineEdit_routline = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_routline.setGeometry(QtCore.QRect(860, 570, 201, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_routline.setFont(font)
        self.lineEdit_routline.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_routline.setObjectName("lineEdit_routline")
        self.lineEdit_mileage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mileage.setGeometry(QtCore.QRect(860, 679, 201, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_mileage.setFont(font)
        self.lineEdit_mileage.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mileage.setObjectName("lineEdit_mileage")
        self.label_mileage = QtWidgets.QLabel(self.centralwidget)
        self.label_mileage.setGeometry(QtCore.QRect(800, 680, 60, 60))
        self.label_mileage.setStyleSheet("border-image: url(:/icon/ui_image/小车已行驶.png);")
        self.label_mileage.setText("")
        self.label_mileage.setObjectName("label_mileage")
        self.button_getcurrentlocal = QtWidgets.QPushButton(self.centralwidget)
        self.button_getcurrentlocal.setGeometry(QtCore.QRect(1070, 460, 101, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_getcurrentlocal.setFont(font)
        self.button_getcurrentlocal.setStyleSheet("QPushButton {\n"
"    \n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(179, 179, 179);\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_getcurrentlocal.setObjectName("button_getcurrentlocal")
        self.button_getmileage = QtWidgets.QPushButton(self.centralwidget)
        self.button_getmileage.setGeometry(QtCore.QRect(1070, 680, 101, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_getmileage.setFont(font)
        self.button_getmileage.setStyleSheet("QPushButton {\n"
"    \n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(179, 179, 179);\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_getmileage.setObjectName("button_getmileage")
        self.button_getrouteline = QtWidgets.QPushButton(self.centralwidget)
        self.button_getrouteline.setGeometry(QtCore.QRect(1070, 570, 101, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_getrouteline.setFont(font)
        self.button_getrouteline.setStyleSheet("QPushButton {\n"
"    \n"
"    border-radius:5px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(179, 179, 179);\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_getrouteline.setObjectName("button_getrouteline")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(1200, 110, 16, 16))
        self.button_exit.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(179, 179, 179);\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_exit.setText("")
        self.button_exit.setObjectName("button_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_return.setText(_translate("MainWindow", "返回"))
        self.label_navigationimage.setText(_translate("MainWindow", "导航路径"))
        self.label.setText(_translate("MainWindow", "待定内容"))
        self.lineEdit_targettask.setPlaceholderText(_translate("MainWindow", "目标任务"))
        self.lineEdit_currentlocal.setPlaceholderText(_translate("MainWindow", "当前位置"))
        self.lineEdit_routline.setPlaceholderText(_translate("MainWindow", "巡视路线"))
        self.lineEdit_mileage.setPlaceholderText(_translate("MainWindow", "小车已行驶"))
        self.button_getcurrentlocal.setText(_translate("MainWindow", "位置获取"))
        self.button_getmileage.setText(_translate("MainWindow", "里程获取"))
        self.button_getrouteline.setText(_translate("MainWindow", "路线获取"))
import resourcesubinterface
