# _*_coding:utf-8_*_
# Author： Zachary
from MainPage_login import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())