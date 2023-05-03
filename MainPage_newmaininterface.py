# _*_coding:utf-8_*_
# Author： Zachary

import os
import subprocess
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView
from newmaininterface import *

class MainInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.setupUI()
        self.retranslateUi()
        # 隐藏窗体
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.ui.button_UAVStatus.click()

    def setupUI(self):
        # 加阴影
        self.ui.frame.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_title.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.frame_8.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.frame_5.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        # 让表格自动适应窗口
        self.ui.tableWidget_Result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_Result.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_DiseaseResult.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_DiseaseResult.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_PatrolData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_PatrolData.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # 这三个方法是鼠标移动事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def retranslateUi(self):
        self.ui.button_Return.clicked.connect(self.return_loginpage)
        self.ui.button_UAVStatus.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.button_RoadCondition.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.button_DiseaseDetection.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.button_PatrolDataManagement.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.button_PatrolReport.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.button_Maximize.clicked.connect(self.page_max_min)


    def return_loginpage(self):
        '''
        实现跳转到sub界面
        :return:
        '''
        self.ui.button_Close.click()
        cur_path = os.path.abspath('./')
        res = subprocess.run(
            fr"python {cur_path}\Main_starter.py", shell=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        sys.exit(self.exec_())

    def page_max_min(self):
        '''
        实现点击放大缩小按钮的功能
        :return:
        '''
        if self.isMaximized():
            self.showNormal()
            self.ui.button_Maximize.setIcon(QtGui.QIcon("./icon/maximize.svg"))
        else:
            self.showMaximized()
            self.ui.button_Maximize.setIcon(QtGui.QIcon("./icon/minimize_recover.svg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    maininterface = MainInterface()
    sys.exit(app.exec_())