# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maininterface.ui'
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
        self.button_storage = QtWidgets.QPushButton(self.centralwidget)
        self.button_storage.setGeometry(QtCore.QRect(150, 130, 61, 61))
        self.button_storage.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    border-image: url(:/icon/ui_image/云存储.png);\n"
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
        self.button_storage.setText("")
        self.button_storage.setObjectName("button_storage")
        self.button_carmessage = QtWidgets.QPushButton(self.centralwidget)
        self.button_carmessage.setGeometry(QtCore.QRect(240, 130, 61, 61))
        self.button_carmessage.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    border-image: url(:/icon/ui_image/小车信息.png);\n"
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
        self.button_carmessage.setText("")
        self.button_carmessage.setObjectName("button_carmessage")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(330, 130, 61, 61))
        self.button_exit.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    border-image: url(:/icon/ui_image/退出.png);\n"
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
"}\n"
"")
        self.button_exit.setText("")
        self.button_exit.setObjectName("button_exit")
        self.label_storage = QtWidgets.QLabel(self.centralwidget)
        self.label_storage.setGeometry(QtCore.QRect(150, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_storage.setFont(font)
        self.label_storage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_storage.setObjectName("label_storage")
        self.label_carmessage = QtWidgets.QLabel(self.centralwidget)
        self.label_carmessage.setGeometry(QtCore.QRect(230, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setKerning(True)
        self.label_carmessage.setFont(font)
        self.label_carmessage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_carmessage.setObjectName("label_carmessage")
        self.label_exit = QtWidgets.QLabel(self.centralwidget)
        self.label_exit.setGeometry(QtCore.QRect(330, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_exit.setFont(font)
        self.label_exit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_exit.setObjectName("label_exit")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(410, 130, 761, 71))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 B")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(24, 20, 65);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_originalimage = QtWidgets.QLabel(self.centralwidget)
        self.label_originalimage.setGeometry(QtCore.QRect(140, 240, 430, 330))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_originalimage.setFont(font)
        self.label_originalimage.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius: 10px;")
        self.label_originalimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_originalimage.setObjectName("label_originalimage")
        self.label_resultimage = QtWidgets.QLabel(self.centralwidget)
        self.label_resultimage.setGeometry(QtCore.QRect(580, 240, 430, 330))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_resultimage.setFont(font)
        self.label_resultimage.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"background-color: rgb(211, 211, 211);\n"
"border-radius: 10px;")
        self.label_resultimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultimage.setObjectName("label_resultimage")
        self.table_result = QtWidgets.QTableWidget(self.centralwidget)
        self.table_result.setGeometry(QtCore.QRect(150, 590, 821, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_result.sizePolicy().hasHeightForWidth())
        self.table_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.table_result.setFont(font)
        self.table_result.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.table_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_result.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_result.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_result.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.table_result.setWordWrap(True)
        self.table_result.setCornerButtonEnabled(True)
        self.table_result.setObjectName("table_result")
        self.table_result.setColumnCount(3)
        self.table_result.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item.setFont(font)
        self.table_result.setItem(3, 2, item)
        self.table_result.horizontalHeader().setVisible(True)
        self.table_result.horizontalHeader().setCascadingSectionResizes(False)
        self.table_result.horizontalHeader().setDefaultSectionSize(256)
        self.table_result.horizontalHeader().setHighlightSections(True)
        self.table_result.horizontalHeader().setMinimumSectionSize(15)
        self.table_result.horizontalHeader().setSortIndicatorShown(False)
        self.table_result.verticalHeader().setSortIndicatorShown(False)
        self.table_result.verticalHeader().setStretchLastSection(False)
        self.label_openfile = QtWidgets.QLabel(self.centralwidget)
        self.label_openfile.setGeometry(QtCore.QRect(1030, 300, 50, 50))
        self.label_openfile.setStyleSheet("border-image: url(:/icon/ui_image/文件.png);")
        self.label_openfile.setText("")
        self.label_openfile.setObjectName("label_openfile")
        self.button_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.button_openfile.setGeometry(QtCore.QRect(1080, 305, 121, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_openfile.setFont(font)
        self.button_openfile.setStyleSheet("QPushButton {\n"
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
        self.button_openfile.setObjectName("button_openfile")
        self.label_refresh = QtWidgets.QLabel(self.centralwidget)
        self.label_refresh.setGeometry(QtCore.QRect(1030, 415, 50, 50))
        self.label_refresh.setStyleSheet("border-image: url(:/icon/ui_image/刷新.png);")
        self.label_refresh.setText("")
        self.label_refresh.setObjectName("label_refresh")
        self.button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_refresh.setGeometry(QtCore.QRect(1080, 420, 121, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_refresh.setFont(font)
        self.button_refresh.setStyleSheet("QPushButton {\n"
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
        self.button_refresh.setObjectName("button_refresh")
        self.button_detect = QtWidgets.QPushButton(self.centralwidget)
        self.button_detect.setGeometry(QtCore.QRect(1080, 535, 121, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_detect.setFont(font)
        self.button_detect.setStyleSheet("QPushButton {\n"
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
        self.button_detect.setObjectName("button_detect")
        self.label_detect = QtWidgets.QLabel(self.centralwidget)
        self.label_detect.setGeometry(QtCore.QRect(1030, 530, 50, 50))
        self.label_detect.setStyleSheet("border-image: url(:/icon/ui_image/检测.png);")
        self.label_detect.setText("")
        self.label_detect.setObjectName("label_detect")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(1030, 645, 50, 50))
        self.label_time.setStyleSheet("border-image: url(:/icon/ui_image/用时.png);")
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")
        self.lineEdit_time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_time.setGeometry(QtCore.QRect(1080, 650, 121, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_time.setFont(font)
        self.lineEdit_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time.setObjectName("lineEdit_time")
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
        self.label_storage.setText(_translate("MainWindow", "存储"))
        self.label_carmessage.setText(_translate("MainWindow", "小车信息"))
        self.label_exit.setText(_translate("MainWindow", "退出"))
        self.label_title.setText(_translate("MainWindow", "基于YOLOv8的道路病害检测系统"))
        self.label_originalimage.setText(_translate("MainWindow", "原始图像"))
        self.label_resultimage.setText(_translate("MainWindow", "检测结果"))
        self.table_result.setSortingEnabled(False)
        item = self.table_result.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "No.1"))
        item = self.table_result.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "No.2"))
        item = self.table_result.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "No.3"))
        item = self.table_result.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "No.4"))
        item = self.table_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.table_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "病害类型"))
        item = self.table_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "置信度"))
        __sortingEnabled = self.table_result.isSortingEnabled()
        self.table_result.setSortingEnabled(False)
        self.table_result.setSortingEnabled(__sortingEnabled)
        self.button_openfile.setText(_translate("MainWindow", "打开文件"))
        self.button_refresh.setText(_translate("MainWindow", "刷新"))
        self.button_detect.setText(_translate("MainWindow", "检测"))
        self.lineEdit_time.setPlaceholderText(_translate("MainWindow", "用时"))
import resourcemaininterface
