import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.uic.properties import QtWidgets, QtCore

from PyQt5 import QtCore, QtGui, QtWidgets

from test.SecondPage import SecondWindow


class UiDialog:
    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.resize(1269, 912)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(200, 190, 721, 91))  # 前两个是坐标，后两个是大小
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: flat;")
        self.textBrowser.setStyleSheet("border-radius: 10px;")

        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(690, 600, 301, 131))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(5, 1, 1267, 908))
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()

        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(35)
        font.setWeight(50)

        self.welcomeButton = QtWidgets.QPushButton(Dialog)
        self.welcomeButton.setText("Enter")  # text
        self.welcomeButton.setIcon(QIcon("D:/青灯/项目/lbx/test/beijing.png"))  # icon
        self.welcomeButton.setToolTip("Close the widget")  # Tool tip
        self.welcomeButton.setGeometry(QtCore.QRect(1000, 610, 160, 100))
        self.welcomeButton.setFlat(True)  # 透明背景
        self.welcomeButton.setFont(font)
        self.welcomeButton.setStyleSheet(
            "QPushButton{color:rgb(101,153,26)}"  # 按键前景色
            "QPushButton{background-color:rgb(198,224,205)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        self.retranslateUi(Dialog)  # 展示方框内的姓名和学号
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        path = "D:/青灯/项目/lbx/test/beijing.png"
        self.show_welcome_image(path)
        self.welcomeButton.clicked.connect(self.on_pushButton1_clicked)

    windowList = []

    # 进入下一个页面的入口函数
    def on_pushButton1_clicked(self):
        the_window = SecondWindow()
        self.windowList.append(the_window)  # 注：没有这句，是不打开另一个主界面的！
        welcome.close()
        the_window.show()

    # 第一个主页面的背景图片
    def show_welcome_image(self, path):
        self.graphicsView.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load(path)
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(1265, 906))  # 自己设定尺寸
        self.graphicsView.scene_img.addItem(self.imgShowItem)
        self.graphicsView.setScene(self.graphicsView.scene_img)
        self.graphicsView.show()

    # 展示方框内的姓名和学号
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" dir=\'rtl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; font-style:italic; color:#00557f;\">欢迎使用穴位识别系统</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#aaaa7f;\">姓名：冯宇静</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#aaaa7f;\">学号：1707004211</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#aaaa7f;\">指导老师：秦品乐</span></p></body></html>"))


class FirstWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('穴位识别')
        self.setWindowIcon(QIcon(r'D:/青灯/项目/lbx/test/beijing.png'))  # 左上角的图标


if __name__ == '__main__':
    my_app = QApplication([])
    welcome = FirstWindow()
    welcome.show()
    # sys.exit(my_app.exec_())
    my_app.exec_()

