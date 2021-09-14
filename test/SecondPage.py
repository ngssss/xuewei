import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QGraphicsScene, QGraphicsPixmapItem


# from PyQt5.uic.properties import QtWidgets


class Loading:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1269, 912)

        # 设置外面的箱子
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(370, 290, 401, 261))
        self.groupBox.setObjectName("groupBox")

        # 设置两个标签:账号，密码
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 70, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 54, 12))
        self.label_2.setObjectName("label_2")

        # 可以设置两条线
        # self.line = QtWidgets.QFrame(self.groupBox)
        # self.line.setGeometry(QtCore.QRect(100, 80, 211, 16))
        # self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        # self.line_2 = QtWidgets.QFrame(self.groupBox)
        # self.line_2.setGeometry(QtCore.QRect(100, 130, 211, 16))
        # self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")

        # 设置输入账号密码的框框
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 100, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)  # 设置密码隐藏

        # 设置两个按钮
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 200, 83, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 200, 83, 35))
        self.pushButton_2.setObjectName("pushButton_2")

        # 设置背景框
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 1, 1267, 908))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.groupBox.raise_()

        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(20)
        font.setWeight(10)

        # 登录按钮的样式
        self.pushButton.setText("登录")  # text

        self.pushButton.setToolTip("Close the widget")  # Tool tip
        self.pushButton.setFlat(True)  # 透明背景
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton{color:rgb(255,140,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(198,224,205)}"  # 按键背景色
            "QPushButton:hover{color:rgb(0,0,205)}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        # 注册按钮的样式
        self.pushButton_2.setText("注册")  # text

        self.pushButton_2.setToolTip("Close the widget")  # Tool tip
        self.pushButton_2.setFlat(True)  # 透明背景
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "QPushButton{color:rgb(255,140,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(198,224,205)}"  # 按键背景色
            "QPushButton:hover{color:rgb(0,0,205)}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        # 布局中间的框框内的UI
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 布局背景用的
        path = r'D:/青灯/项目/lbx/test/beijing.png'
        self.show_welcome_image(path)

        # 设置登录按钮函数
        self.pushButton.clicked.connect(self.on_pushButton1_clicked)

    windowList = []

    # UI布局
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "欢迎使用穴位识别系统"))
        self.label.setText(_translate("Dialog", "账号"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "注册"))

    # 设置背景
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

    # 设置登录函数
    def on_pushButton1_clicked(self):
        pass
        # the_window = MainWindow()
        # self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # second_window.close()
        # the_window.show()

        # 默认显示标准图像


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Loading()
        self.ui.setupUi(self)
        self.setWindowTitle("穴位识别")
        self.setWindowIcon(QIcon(r'D:/青灯/项目/lbx/test/beijing.png'))  # 左上角的图标


if __name__ == '__main__':
    myapp = QApplication([])
    second_window = SecondWindow()
    second_window.show()
    # sys.exit(myapp.exec_())
    myapp.exec_()
