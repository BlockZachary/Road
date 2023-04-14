# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(170, 110, 551, 421))
        self.background_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.login_usr = QtWidgets.QLineEdit(self.centralwidget)
        self.login_usr.setGeometry(QtCore.QRect(330, 310, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.login_usr.setFont(font)
        self.login_usr.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(128, 128, 128);")
        self.login_usr.setText("")
        self.login_usr.setObjectName("login_usr")
        self.login_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.login_pwd.setGeometry(QtCore.QRect(330, 360, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.login_pwd.setFont(font)
        self.login_pwd.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255,0);\n"
"border-bottom: 1px solid rgb(0, 0, 0);\n"
"color: rgb(128, 128, 128);")
        self.login_pwd.setText("")
        self.login_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_pwd.setObjectName("login_pwd")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(320, 440, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    background-color: rgb(3, 187, 252);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(104, 214, 253);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_login.setObjectName("button_login")
        self.button_register = QtWidgets.QPushButton(self.centralwidget)
        self.button_register.setGeometry(QtCore.QRect(450, 440, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.button_register.setFont(font)
        self.button_register.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    background-color: rgb(128, 128, 128);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color:rgb(179, 179, 179);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:5px;\n"
"}")
        self.button_register.setObjectName("button_register")
        self.colorbackground_label = QtWidgets.QLabel(self.centralwidget)
        self.colorbackground_label.setGeometry(QtCore.QRect(170, 110, 551, 181))
        self.colorbackground_label.setStyleSheet("background-color: rgb(51, 203, 255);\n"
"border-top-right-radius:5px;\n"
"border-top-left-radius:5px;")
        self.colorbackground_label.setText("")
        self.colorbackground_label.setObjectName("colorbackground_label")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(180, 120, 92, 89))
        self.logo_label.setStyleSheet("border-image: url(:/image/ui_image/logo.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 210, 551, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(24, 20, 65);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 320, 25, 25))
        self.label_2.setStyleSheet("border-image: url(:/icon/ui_image/用户_user.svg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 370, 25, 25))
        self.label_3.setStyleSheet("border-image: url(:/icon/ui_image/锁定_lock.svg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(680, 120, 30, 30))
        self.button_close.setStyleSheet("QPushButton {\n"
"    border-image: url(:/icon/ui_image/关闭-小_close-small.svg);\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color:rgb(179, 179, 179);\n"
"}")
        self.button_close.setText("")
        self.button_close.setObjectName("button_close")
        self.button_lower = QtWidgets.QPushButton(self.centralwidget)
        self.button_lower.setGeometry(QtCore.QRect(650, 130, 20, 20))
        self.button_lower.setStyleSheet("QPushButton {\n"
"    border-image: url(:/icon/ui_image/Minimize-2.svg);\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color:rgb(179, 179, 179);\n"
"}")
        self.button_lower.setText("")
        self.button_lower.setObjectName("button_lower")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button_close.clicked.connect(MainWindow.close)
        self.button_lower.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_usr.setPlaceholderText(_translate("MainWindow", "用户名："))
        self.login_pwd.setPlaceholderText(_translate("MainWindow", "密码："))
        self.button_login.setText(_translate("MainWindow", "登录"))
        self.button_register.setText(_translate("MainWindow", "注册"))
        self.label.setText(_translate("MainWindow", "基于YOLOv8的道路病害检测系统"))
import resourcelogin
