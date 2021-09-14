import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QGraphicsPixmapItem, QGraphicsScene
from test.GraphicsView import GraphicsView
import cv2
import numpy as np

import scaling2

# from .playUI import Ui_Form

"""
    需传到算法执行部分的全局变量
"""
imageZ = ''
imageB = ''


class Ui_MainWindow:
    imgUrl = ''

    # UI标签设置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 912)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.XZButton = QtWidgets.QPushButton(self.centralwidget)
        self.XZButton.setMinimumSize(QtCore.QSize(155, 40))
        self.XZButton.setObjectName("XZButton")
        self.XZButton.setCheckable(True)
        self.verticalLayout_2.addWidget(self.XZButton)

        self.XBButton = QtWidgets.QPushButton(self.centralwidget)
        self.XBButton.setMinimumSize(QtCore.QSize(155, 40))
        self.XBButton.setObjectName("XBButton")
        self.verticalLayout_2.addWidget(self.XBButton)

        self.DoButton = QtWidgets.QPushButton(self.centralwidget)
        self.DoButton.setMinimumSize(QtCore.QSize(155, 40))
        self.DoButton.setObjectName("DoButton")
        self.verticalLayout_2.addWidget(self.DoButton)

        self.ZPlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZPlayButton.setMinimumSize(QtCore.QSize(155, 40))
        self.ZPlayButton.setObjectName("ZPlayButton")
        self.verticalLayout_2.addWidget(self.ZPlayButton)

        self.BPlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.BPlayButton.setMinimumSize(QtCore.QSize(155, 40))
        self.BPlayButton.setObjectName("BPlayButton")
        self.verticalLayout_2.addWidget(self.BPlayButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # 正面标准图
        self.ZstandardView = GraphicsView()
        #
        # self.ZstandardView = QtWidgets.QGraphicsView(self.groupBox_3)
        self.ZstandardView.setObjectName("ZstandardView")
        self.verticalLayout_5.addWidget(self.ZstandardView)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(100, 25))
        self.textBrowser_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_5.addWidget(self.textBrowser_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # 正面测试图
        self.ZtestView = GraphicsView()
        self.ZtestView.setObjectName("ZtestView")
        self.verticalLayout_6.addWidget(self.ZtestView)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(100, 25))
        self.textBrowser_7.setSizeIncrement(QtCore.QSize(0, 0))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.verticalLayout_6.addWidget(self.textBrowser_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # 正面标注完成图
        self.ZdonetestView = GraphicsView()
        self.ZdonetestView.setObjectName("ZdonetestView")
        self.verticalLayout_7.addWidget(self.ZdonetestView)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_8.setMaximumSize(QtCore.QSize(100, 25))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.verticalLayout_7.addWidget(self.textBrowser_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # 背面标准图
        self.BstandardView = GraphicsView()
        self.BstandardView.setObjectName("BstandardView")
        self.verticalLayout.addWidget(self.BstandardView)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(100, 25))
        self.textBrowser_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # 背面测试图
        self.BtestView = GraphicsView()
        self.BtestView.setObjectName("BtestView")
        self.verticalLayout_3.addWidget(self.BtestView)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(100, 25))
        self.textBrowser_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_3.addWidget(self.textBrowser_5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # 背面已标注图
        self.BdonetestView = GraphicsView()
        self.BdonetestView.setObjectName("BdonetestView")
        self.verticalLayout_4.addWidget(self.BdonetestView)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(100, 25))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.XZButton.raise_()
        self.XBButton.raise_()
        self.DoButton.raise_()
        self.ZPlayButton.raise_()
        self.BPlayButton.raise_()
        self.DoButton.raise_()
        self.BPlayButton.raise_()
        self.ZPlayButton.raise_()
        self.DoButton.raise_()
        self.XBButton.raise_()
        self.XZButton.raise_()
        self.groupBox_3.raise_()
        self.ZPlayButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.XZButton.clicked.connect(self.select_button_clicked)
        self.XBButton.clicked.connect(self.select_button_clicked2)
        self.DoButton.clicked.connect(self.identify_button_clicked)
        self.ZPlayButton.clicked.connect(self.show_button_clicked)
        self.BPlayButton.clicked.connect(self.show_buttonb_clicked)

        self.msg_box = QMessageBox(QMessageBox.Warning, '提示', '穴位识别结束')

        # 展示正、反面标准图
        path1 = './1.png'
        path2 = './2.jpg'
        self.show_standard_image(path1)
        self.show_standard_back_image(path2)

    # 跳转正面展示界面
    windowList = []

    # def on_pushButton1_clicked(self):
    #     the_window = ZPlayDialog()
    #     self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
    #     the_window.show()
    #
    # def on_BpushButton1_clicked(self):
    #     the_window = PlayDialog()
    #     self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
    #     the_window.show()
    """由page2跳转这个页面"""
    # 布局UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.XZButton.setText(_translate("MainWindow", "选择正面识别图像"))
        self.XZButton.setStyleSheet("background-color:rgb(111,180,219)")
        self.XZButton.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        self.XBButton.setText(_translate("MainWindow", "选择背面识别图像"))
        self.XBButton.setStyleSheet("background-color:rgb(111,180,219)")
        self.XBButton.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        self.DoButton.setText(_translate("MainWindow", "穴位识别"))
        self.DoButton.setStyleSheet("background-color:rgb(111,180,219)")
        self.DoButton.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        self.BPlayButton.setText(_translate("MainWindow", "背面穴位详情展示"))
        self.BPlayButton.setStyleSheet("background-color:rgb(111,180,219)")
        self.BPlayButton.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        self.ZPlayButton.setText(_translate("MainWindow", "正面穴位详情展示"))
        self.ZPlayButton.setStyleSheet("background-color:rgb(111,180,219)")
        self.ZPlayButton.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        self.groupBox_3.setTitle(_translate("MainWindow", "正面"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">标准穴位图</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">待标注图片</p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">标注完成图片</p></body></html>"))

        self.groupBox_2.setTitle(_translate("MainWindow", "背面"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">标准穴位图</p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">待标注图片</p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">标注完成图片</p></body></html>"))

    # 默认显示标准图像(正)
    def show_standard_image(self, path):
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
        self.ZstandardView.change_image(img)
        self.ZstandardView.show()

    # 默认显示标准图像(反)
    def show_standard_back_image(self, path):
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
        self.BstandardView.change_image(img)
        self.BstandardView.show()

    # 选择正面图像识别
    def select_button_clicked(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "D:/MyStudy/gp_picture", "jpg (*.jpg)")
        global imageZ
        imageZ = file_name[0]
        Ui_MainWindow.imgUrl = file_name[0]
        # img = cv2.imread(imageZ)  # 读取图像 函数不能读中文文件名文件
        img = cv2.imdecode(np.fromfile(imageZ, dtype=np.uint8), -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ZtestView.setScene(self.scene)
        self.ZtestView.change_image(img)
        self.ZtestView.show()

    # 选择反面图像识别
    def select_button_clicked2(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "D:/MyStudy/gp_picture", "jpg (*.jpg)")

        global imageB
        imageB = file_name[0]

        # img = cv2.imread(imageB)  # 读取图像 函数不能读中文文件名文件
        img = cv2.imdecode(np.fromfile(imageB, dtype=np.uint8), -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.BtestView.setScene(self.scene)
        self.BtestView.change_image(img)
        self.BtestView.show()

    """
        获取两个路径
        并把这两个路径传递到 scaling
        并获取两个路径传递到两个view
    """
    # 图像穴位识别
    # def identify_button_clicked(self, scaling2=None):
    def identify_button_clicked(self):
        print('xy')
        scaling2.scale(imageZ, imageB)
        print('2')
        print("scaling2.body_parts1", scaling2.body_parts1)
        if scaling2.flag == 58:
            # self.msg_box.show()
            # sys.exit(msg_box.exec_())

            pathZ = 'D:/MyStudy/Github_source/aip-python-sdk-4.15.1/UI/tomarkZ.png'
            imgZ = cv2.imdecode(np.fromfile(pathZ, dtype=np.uint8), 1)
            self.ZdonetestView.change_image(imgZ)
            self.ZdonetestView.show()

            pathB = 'D:/MyStudy/Github_source/aip-python-sdk-4.15.1/UI/tomarkB.png'
            imgB = cv2.imdecode(np.fromfile(pathB, dtype=np.uint8), 1)
            self.BdonetestView.change_image(imgB)
            self.BdonetestView.show()

    # 显示标注结果
    def show_button_clicked(self):
        path1 = 'tomarkZ.png'
        img1 = cv2.imdecode(np.fromfile(path1, dtype=np.uint8), 1)
        self.ZdonetestView.change_image(img1)
        self.ZdonetestView.show()

    def show_buttonb_clicked(self):
        path1 = 'tomarkB.png'
        img1 = cv2.imdecode(np.fromfile(path1, dtype=np.uint8), 1)
        self.BdonetestView.change_image(img1)
        self.BdonetestView.show()


"""
    正面结果展示界面
"""


class Ui_ZDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1121, 890)

        self.ZPlay = QtWidgets.QGraphicsView(Dialog)
        self.ZPlay.setGeometry(QtCore.QRect(50, 30, 560, 760))
        self.ZPlay.setMinimumSize(QtCore.QSize(560, 760))
        self.ZPlay.setMaximumSize(QtCore.QSize(560, 760))
        self.ZPlay.setObjectName("ZPlay")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 60, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_30 = QtWidgets.QPushButton(Dialog)
        self.pushButton_30.setGeometry(QtCore.QRect(30, 470, 60, 20))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_28 = QtWidgets.QPushButton(Dialog)
        self.pushButton_28.setGeometry(QtCore.QRect(110, 330, 60, 20))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 60, 60, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_25 = QtWidgets.QPushButton(Dialog)
        self.pushButton_25.setGeometry(QtCore.QRect(110, 310, 60, 20))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_31 = QtWidgets.QPushButton(Dialog)
        self.pushButton_31.setGeometry(QtCore.QRect(30, 500, 60, 20))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 60, 60, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 120, 60, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_41 = QtWidgets.QPushButton(Dialog)
        self.pushButton_41.setGeometry(QtCore.QRect(30, 560, 60, 20))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_33 = QtWidgets.QPushButton(Dialog)
        self.pushButton_33.setGeometry(QtCore.QRect(30, 380, 60, 20))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_39 = QtWidgets.QPushButton(Dialog)
        self.pushButton_39.setGeometry(QtCore.QRect(30, 530, 60, 20))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(110, 430, 60, 20))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(110, 410, 60, 20))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 20, 60, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_46 = QtWidgets.QPushButton(Dialog)
        self.pushButton_46.setGeometry(QtCore.QRect(390, 890, 60, 20))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(110, 230, 60, 20))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_47 = QtWidgets.QPushButton(Dialog)
        self.pushButton_47.setGeometry(QtCore.QRect(390, 950, 60, 20))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_38 = QtWidgets.QPushButton(Dialog)
        self.pushButton_38.setGeometry(QtCore.QRect(30, 290, 60, 20))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(550, 20, 60, 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_23 = QtWidgets.QPushButton(Dialog)
        self.pushButton_23.setGeometry(QtCore.QRect(110, 210, 60, 20))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_36 = QtWidgets.QPushButton(Dialog)
        self.pushButton_36.setGeometry(QtCore.QRect(30, 260, 60, 20))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_40 = QtWidgets.QPushButton(Dialog)
        self.pushButton_40.setGeometry(QtCore.QRect(30, 170, 60, 20))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(550, 80, 60, 20))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_32 = QtWidgets.QPushButton(Dialog)
        self.pushButton_32.setGeometry(QtCore.QRect(30, 410, 60, 20))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_37 = QtWidgets.QPushButton(Dialog)
        self.pushButton_37.setGeometry(QtCore.QRect(30, 350, 60, 20))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_26 = QtWidgets.QPushButton(Dialog)
        self.pushButton_26.setGeometry(QtCore.QRect(110, 270, 60, 20))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_29 = QtWidgets.QPushButton(Dialog)
        self.pushButton_29.setGeometry(QtCore.QRect(30, 440, 60, 20))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(110, 390, 60, 20))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(550, 40, 60, 20))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_24 = QtWidgets.QPushButton(Dialog)
        self.pushButton_24.setGeometry(QtCore.QRect(110, 250, 60, 20))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(110, 370, 60, 20))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_45 = QtWidgets.QPushButton(Dialog)
        self.pushButton_45.setGeometry(QtCore.QRect(390, 920, 60, 20))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(550, 140, 60, 20))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_21 = QtWidgets.QPushButton(Dialog)
        self.pushButton_21.setGeometry(QtCore.QRect(110, 470, 60, 20))
        self.pushButton_21.setObjectName("pushButton_21")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(1130, 470, 341, 351))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_43 = QtWidgets.QPushButton(Dialog)
        self.pushButton_43.setGeometry(QtCore.QRect(30, 590, 60, 20))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 140, 60, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_44 = QtWidgets.QPushButton(Dialog)
        self.pushButton_44.setGeometry(QtCore.QRect(390, 980, 60, 20))
        self.pushButton_44.setObjectName("pushButton_44")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(1130, 410, 191, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_27 = QtWidgets.QPushButton(Dialog)
        self.pushButton_27.setGeometry(QtCore.QRect(110, 290, 60, 20))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(110, 450, 60, 20))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_42 = QtWidgets.QPushButton(Dialog)
        self.pushButton_42.setGeometry(QtCore.QRect(30, 320, 60, 20))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 100, 60, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(550, 120, 60, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(110, 350, 60, 20))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 80, 60, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_34 = QtWidgets.QPushButton(Dialog)
        self.pushButton_34.setGeometry(QtCore.QRect(30, 200, 60, 20))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 100, 60, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_35 = QtWidgets.QPushButton(Dialog)
        self.pushButton_35.setGeometry(QtCore.QRect(30, 230, 60, 20))
        self.pushButton_35.setObjectName("pushButton_35")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(770, 30, 191, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(770, 80, 341, 351))
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        path = 'D:/MyStudy/tomarkZ.png'
        self.show_image(path)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "后顶"))
        self.pushButton_30.setText(_translate("Dialog", "胃俞"))
        self.pushButton_28.setText(_translate("Dialog", "筋缩"))
        self.pushButton_9.setText(_translate("Dialog", "脑空"))
        self.pushButton_25.setText(_translate("Dialog", "至阳"))
        self.pushButton_31.setText(_translate("Dialog", "三焦俞"))
        self.pushButton_3.setText(_translate("Dialog", "强间"))
        self.pushButton_7.setText(_translate("Dialog", "哑门"))
        self.pushButton_41.setText(_translate("Dialog", "气海俞"))
        self.pushButton_33.setText(_translate("Dialog", "肝俞"))
        self.pushButton_39.setText(_translate("Dialog", "肾俞"))
        self.pushButton_20.setText(_translate("Dialog", "腰阳关"))
        self.pushButton_19.setText(_translate("Dialog", "命门"))
        self.pushButton.setText(_translate("Dialog", "百会"))
        self.pushButton_46.setText(_translate("Dialog", "三焦俞"))
        self.pushButton_22.setText(_translate("Dialog", "陶道"))
        self.pushButton_47.setText(_translate("Dialog", "气海俞"))
        self.pushButton_38.setText(_translate("Dialog", "心俞"))
        self.pushButton_10.setText(_translate("Dialog", "络却"))
        self.pushButton_23.setText(_translate("Dialog", "大椎"))
        self.pushButton_36.setText(_translate("Dialog", "厥阴俞"))
        self.pushButton_40.setText(_translate("Dialog", "大抒"))
        self.pushButton_11.setText(_translate("Dialog", "凤池"))
        self.pushButton_32.setText(_translate("Dialog", "胆俞"))
        self.pushButton_37.setText(_translate("Dialog", "膈俞"))
        self.pushButton_26.setText(_translate("Dialog", "神道"))
        self.pushButton_29.setText(_translate("Dialog", "脾俞"))
        self.pushButton_17.setText(_translate("Dialog", "悬枢"))
        self.pushButton_13.setText(_translate("Dialog", "玉枕"))
        self.pushButton_24.setText(_translate("Dialog", "身柱"))
        self.pushButton_15.setText(_translate("Dialog", "脊中"))
        self.pushButton_45.setText(_translate("Dialog", "肾俞"))
        self.pushButton_12.setText(_translate("Dialog", "完骨"))
        self.pushButton_21.setText(_translate("Dialog", "完骨"))
        self.pushButton_43.setText(_translate("Dialog", "大肠俞"))
        self.pushButton_6.setText(_translate("Dialog", "天柱"))
        self.pushButton_44.setText(_translate("Dialog", "大肠俞"))
        self.pushButton_27.setText(_translate("Dialog", "灵台"))
        self.pushButton_18.setText(_translate("Dialog", "腰俞"))
        self.pushButton_42.setText(_translate("Dialog", "督俞"))
        self.pushButton_5.setText(_translate("Dialog", "风府"))
        self.pushButton_14.setText(_translate("Dialog", "头窍阴"))
        self.pushButton_16.setText(_translate("Dialog", "中枢"))
        self.pushButton_4.setText(_translate("Dialog", "脑户"))
        self.pushButton_34.setText(_translate("Dialog", "风门"))
        self.pushButton_8.setText(_translate("Dialog", "浮白"))
        self.pushButton_35.setText(_translate("Dialog", "肺俞"))

    def show_image(self, path):
        # img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
        self.ZPlay.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load(path)
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(550, 750))  # 自己设定尺寸
        self.ZPlay.scene_img.addItem(self.imgShowItem)
        self.ZPlay.setScene(self.ZPlay.scene_img)
        self.ZPlay.show()


"""
    背面结果展示界面
"""


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 898)

        self.graphicsView = QtWidgets.QGraphicsView(Form)
        # self.graphicsView = GraphicsView()
        self.graphicsView.setGeometry(QtCore.QRect(70, 30, 441, 811))
        self.graphicsView.setObjectName("graphicsView")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(780, 140, 191, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(780, 200, 341, 351))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 60, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 40, 60, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 60, 60, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 80, 60, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 100, 60, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 140, 60, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 120, 60, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 90, 60, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(510, 50, 60, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(510, 10, 60, 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(510, 70, 60, 20))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 130, 60, 20))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(510, 30, 60, 20))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(510, 110, 60, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(120, 370, 60, 20))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(120, 350, 60, 20))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(120, 390, 60, 20))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(120, 450, 60, 20))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(120, 410, 60, 20))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(120, 430, 60, 20))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(120, 470, 60, 20))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setGeometry(QtCore.QRect(120, 230, 60, 20))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setGeometry(QtCore.QRect(120, 210, 60, 20))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setGeometry(QtCore.QRect(120, 250, 60, 20))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(Form)
        self.pushButton_25.setGeometry(QtCore.QRect(120, 310, 60, 20))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(Form)
        self.pushButton_26.setGeometry(QtCore.QRect(120, 270, 60, 20))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(Form)
        self.pushButton_27.setGeometry(QtCore.QRect(120, 290, 60, 20))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(Form)
        self.pushButton_28.setGeometry(QtCore.QRect(120, 330, 60, 20))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(Form)
        self.pushButton_29.setGeometry(QtCore.QRect(40, 440, 60, 20))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(Form)
        self.pushButton_30.setGeometry(QtCore.QRect(40, 470, 60, 20))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(Form)
        self.pushButton_31.setGeometry(QtCore.QRect(40, 500, 60, 20))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(Form)
        self.pushButton_32.setGeometry(QtCore.QRect(40, 410, 60, 20))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(Form)
        self.pushButton_33.setGeometry(QtCore.QRect(40, 380, 60, 20))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(Form)
        self.pushButton_34.setGeometry(QtCore.QRect(40, 200, 60, 20))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(Form)
        self.pushButton_35.setGeometry(QtCore.QRect(40, 230, 60, 20))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(Form)
        self.pushButton_36.setGeometry(QtCore.QRect(40, 260, 60, 20))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(Form)
        self.pushButton_37.setGeometry(QtCore.QRect(40, 350, 60, 20))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(Form)
        self.pushButton_38.setGeometry(QtCore.QRect(40, 290, 60, 20))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(Form)
        self.pushButton_39.setGeometry(QtCore.QRect(40, 530, 60, 20))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(Form)
        self.pushButton_40.setGeometry(QtCore.QRect(40, 170, 60, 20))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(Form)
        self.pushButton_41.setGeometry(QtCore.QRect(40, 560, 60, 20))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(Form)
        self.pushButton_42.setGeometry(QtCore.QRect(40, 320, 60, 20))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(Form)
        self.pushButton_43.setGeometry(QtCore.QRect(40, 590, 60, 20))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(Form)
        self.pushButton_44.setGeometry(QtCore.QRect(40, 710, 60, 20))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(Form)
        self.pushButton_45.setGeometry(QtCore.QRect(40, 650, 60, 20))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(Form)
        self.pushButton_46.setGeometry(QtCore.QRect(40, 620, 60, 20))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(Form)
        self.pushButton_47.setGeometry(QtCore.QRect(40, 680, 60, 20))
        self.pushButton_47.setObjectName("pushButton_47")
        self.graphicsView.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.pushButton_2.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_24.raise_()
        self.pushButton_26.raise_()
        self.pushButton_28.raise_()
        self.pushButton_27.raise_()
        self.pushButton_23.raise_()
        self.pushButton_25.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_37.raise_()
        self.pushButton_38.raise_()
        self.pushButton_39.raise_()
        self.pushButton_40.raise_()
        self.pushButton_41.raise_()
        self.pushButton_42.raise_()
        self.pushButton_43.raise_()
        self.pushButton_44.raise_()
        self.pushButton_45.raise_()
        self.pushButton_46.raise_()
        self.pushButton_47.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.show_back_image()

        # 默认显示标准图像

    def show_back_image(self):
        fileName = 'D:/MyStudy/tomarkB.png'
        # fileName = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
        self.graphicsView.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load(fileName)
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        # self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(8000,  8000))    //自己设定尺寸
        self.graphicsView.scene_img.addItem(self.imgShowItem)
        self.graphicsView.setScene(self.graphicsView.scene_img)
        self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "百会"))
        self.pushButton_2.setText(_translate("Form", "后顶"))
        self.pushButton_3.setText(_translate("Form", "强间"))
        self.pushButton_4.setText(_translate("Form", "脑户"))
        self.pushButton_5.setText(_translate("Form", "风府"))
        self.pushButton_6.setText(_translate("Form", "天柱"))
        self.pushButton_7.setText(_translate("Form", "哑门"))
        self.pushButton_8.setText(_translate("Form", "浮白"))
        self.pushButton_9.setText(_translate("Form", "脑空"))
        self.pushButton_10.setText(_translate("Form", "络却"))
        self.pushButton_11.setText(_translate("Form", "凤池"))
        self.pushButton_12.setText(_translate("Form", "完骨"))
        self.pushButton_13.setText(_translate("Form", "玉枕"))
        self.pushButton_14.setText(_translate("Form", "头窍阴"))
        self.pushButton_15.setText(_translate("Form", "脊中"))
        self.pushButton_16.setText(_translate("Form", "中枢"))
        self.pushButton_17.setText(_translate("Form", "悬枢"))
        self.pushButton_18.setText(_translate("Form", "腰俞"))
        self.pushButton_19.setText(_translate("Form", "命门"))
        self.pushButton_20.setText(_translate("Form", "腰阳关"))
        self.pushButton_21.setText(_translate("Form", "完骨"))
        self.pushButton_22.setText(_translate("Form", "陶道"))
        self.pushButton_23.setText(_translate("Form", "大椎"))
        self.pushButton_24.setText(_translate("Form", "身柱"))
        self.pushButton_25.setText(_translate("Form", "至阳"))
        self.pushButton_26.setText(_translate("Form", "神道"))
        self.pushButton_27.setText(_translate("Form", "灵台"))
        self.pushButton_28.setText(_translate("Form", "筋缩"))
        self.pushButton_29.setText(_translate("Form", "脾俞"))
        self.pushButton_30.setText(_translate("Form", "胃俞"))
        self.pushButton_31.setText(_translate("Form", "三焦俞"))
        self.pushButton_32.setText(_translate("Form", "胆俞"))
        self.pushButton_33.setText(_translate("Form", "肝俞"))
        self.pushButton_34.setText(_translate("Form", "风门"))
        self.pushButton_35.setText(_translate("Form", "肺俞"))
        self.pushButton_36.setText(_translate("Form", "厥阴俞"))
        self.pushButton_37.setText(_translate("Form", "膈俞"))
        self.pushButton_38.setText(_translate("Form", "心俞"))
        self.pushButton_39.setText(_translate("Form", "肾俞"))
        self.pushButton_40.setText(_translate("Form", "大抒"))
        self.pushButton_41.setText(_translate("Form", "气海俞"))
        self.pushButton_42.setText(_translate("Form", "督俞"))
        self.pushButton_43.setText(_translate("Form", "大肠俞"))
        self.pushButton_44.setText(_translate("Form", "大肠俞"))
        self.pushButton_45.setText(_translate("Form", "肾俞"))
        self.pushButton_46.setText(_translate("Form", "三焦俞"))
        self.pushButton_47.setText(_translate("Form", "气海俞"))


##################################################################################################
"""
    运行界面
"""


##################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('穴位识别')
        self.setWindowIcon(QIcon(r'D:/青灯/项目/lbx/test/beijing.png'))  # 左上角的图标
        self.show()


class PlayDialog(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('穴位识别')
        self.setWindowIcon(QIcon('D:/MyStudy/gp_picture/mylogo.png'))


class ZPlayDialog(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_ZDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('穴位识别')
        self.setWindowIcon(QIcon('D:/MyStudy/gp_picture/mylogo.png'))


if __name__ == '__main__':
    myapp = QApplication([])
    main_window = MainWindow()
    main_window.show()
    myapp.exec_()
