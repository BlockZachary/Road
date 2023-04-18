# _*_coding:utf-8_*_
# Author： Zachary
import os
import subprocess
import sys

import pymysql
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login import *


class Login(QMainWindow):
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

    def setupUI(self):
        # 加阴影
        self.ui.background_label.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.button_login.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.button_register.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

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
        self.ui.button_login.clicked.connect(self.login_fct)
        self.ui.button_register.clicked.connect(self.register_fct)

    def login_fct(self):
        '''
        登录按钮功能实现
        :return:
        '''
        self.conn_mysql()
        usr = self.ui.login_usr.text()
        pwd = self.ui.login_pwd.text()

        if not usr or not pwd:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "请输入完整的用户名和密码!")
            msg_box.setWindowIcon(QtGui.QIcon('./icon/warning.ico'))
            msg_box.exec_()
            return

        my_query = "SELECT * FROM user WHERE username = %s"
        self.cursor.execute(my_query, [usr])
        res = self.cursor.fetchall()

        if res:
            my_query = "SELECT * FROM user WHERE username = %s and password = %s"
            self.cursor.execute(my_query, [usr, pwd])
            res = self.cursor.fetchall()
            self.conn.close()
            if res:
                self.ui.button_close.click()
                cur_path = os.path.abspath('./')
                res = subprocess.run(
                    fr"python {cur_path}\MainPage_maininterface.py", shell=True,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
                sys.exit(self.exec_())
            else:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "密码错误，请重试!")
                msg_box.setWindowIcon(QtGui.QIcon('./icon/warning.ico'))
                msg_box.exec_()
                self.ui.login_pwd.setText("")
                return
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "用户名不存在请先注册!")
            msg_box.setWindowIcon(QtGui.QIcon('./icon/warning.ico'))
            msg_box.exec_()
            self.ui.login_usr.setText("")
            self.ui.login_pwd.setText("")
            return

    def register_fct(self):
        '''
        注册按钮功能实现
        :return:
        '''
        self.conn_mysql()
        usr = self.ui.login_usr.text()
        pwd = self.ui.login_pwd.text()

        if not usr or not pwd:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "请输入完整的用户名和密码!")
            msg_box.setWindowIcon(QtGui.QIcon('./icon/warning.ico'))
            msg_box.exec_()
            return

        my_query = "SELECT * FROM user WHERE username = %s"
        self.cursor.execute(my_query, [usr])
        res = self.cursor.fetchall()

        if res:
            msg_box = QMessageBox(QMessageBox.Warning, "Warning", "用户已经存在!\n请登录，或者重新输入用户名！")
            msg_box.setWindowIcon(QtGui.QIcon('./icon/warning.ico'))
            msg_box.exec_()
            self.ui.login_usr.setText("")
            self.ui.login_pwd.setText("")
            self.conn.close()
            return
        else:
            my_insert = "INSERT INTO user(username,password) VALUES(%s,%s)"
            self.cursor.execute(my_insert, [usr, pwd])
            self.conn.commit()
            msg_box = QMessageBox(QMessageBox.Warning, "Success", "新用户已注册成功！")
            msg_box.setWindowIcon(QtGui.QIcon('./icon/success.ico'))
            msg_box.exec_()
        self.conn.close()

    def conn_mysql(self):
        '''
        创建mysql连接的函数
        :return:
        '''
        self.conn = pymysql.connect(host='localhost', user='root', password='980226', database='road', use_unicode=True)
        self.cursor = self.conn.cursor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())
