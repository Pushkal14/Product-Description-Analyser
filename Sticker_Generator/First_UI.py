from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont
import os

# TODO: Generate sticker of size with respect to number of rows in it.

# v11: left column for attributes
# v12: right column for values

class Ui_MainWindow(object):
    record_count = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(26, 20, 751, 30))
        self.label_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_title.setTextFormat(QtCore.Qt.RichText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(359, 80, 321, 400))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vl2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vl2.setContentsMargins(10, 10, 10, 10)
        self.vl2.setSpacing(2)
        self.vl2.setObjectName("vl2")

        self.textinput_vl2 = [QtWidgets.QLineEdit(self.verticalLayoutWidget_2)]
        self.textinput_vl2[self.record_count].setObjectName("textinput_vl2_" + str(self.record_count))

        self.vl2.addWidget(self.textinput_vl2[self.record_count])
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 80, 321, 400))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.vl1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vl1.setContentsMargins(10, 10, 10, 10)
        self.vl1.setSpacing(2)
        self.vl1.setObjectName("vl1")
        self.textinput_vl1 = [QtWidgets.QLineEdit(self.verticalLayoutWidget_3)]
        self.textinput_vl1[self.record_count].setEnabled(True)
        self.textinput_vl1[self.record_count].setText("")
        self.textinput_vl1[self.record_count].setObjectName("textinput_vl1_" + str(self.record_count))

        self.vl1.addWidget(self.textinput_vl1[self.record_count])
        self.btn_addRecord = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addRecord.setGeometry(QtCore.QRect(700, 90, 81, 41))
        self.btn_addRecord.setObjectName("btn_addRecord")
        self.btn_removeRecord = QtWidgets.QPushButton(self.centralwidget)
        self.btn_removeRecord.setGeometry(QtCore.QRect(700, 144, 81, 41))
        self.btn_removeRecord.setObjectName("btn_removeRecord")
        self.btn_okCancel = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.btn_okCancel.setGeometry(QtCore.QRect(625, 512, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_okCancel.sizePolicy().hasHeightForWidth())
        self.btn_okCancel.setSizePolicy(sizePolicy)
        self.btn_okCancel.setOrientation(QtCore.Qt.Horizontal)
        self.btn_okCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btn_okCancel.setCenterButtons(False)
        self.btn_okCancel.setObjectName("btn_okCancel")
        self.label_Attribute = QtWidgets.QLabel(self.centralwidget)
        self.label_Attribute.setGeometry(QtCore.QRect(140, 60, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Attribute.sizePolicy().hasHeightForWidth())
        self.label_Attribute.setSizePolicy(sizePolicy)
        self.label_Attribute.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Attribute.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Attribute.setTextFormat(QtCore.Qt.RichText)
        self.label_Attribute.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Attribute.setObjectName("label_Attribute")
        self.label_values = QtWidgets.QLabel(self.centralwidget)
        self.label_values.setGeometry(QtCore.QRect(500, 64, 47, 13))
        self.label_values.setTextFormat(QtCore.Qt.RichText)
        self.label_values.setAlignment(QtCore.Qt.AlignCenter)
        self.label_values.setObjectName("label_values")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        # self.menuFile = QtWidgets.QMenu(self.menubar)
        # self.menuFile.setObjectName("menuFile")
        # self.menuStorage = QtWidgets.QMenu(self.menubar)
        # self.menuStorage.setObjectName("menuStorage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.menubar.addAction(self.menuFile.menuAction())
        # self.menubar.addAction(self.menuStorage.menuAction())

        self.label_no_of_stickers = QtWidgets.QLabel(self.centralwidget)
        self.label_no_of_stickers.setGeometry(QtCore.QRect(40, 505, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_no_of_stickers.setFont(font)
        self.label_no_of_stickers.setObjectName("label_no_of_stickers")

        self.spinBox_no_of_stickers = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_no_of_stickers.setGeometry(QtCore.QRect(180, 500, 71, 31))
        self.spinBox_no_of_stickers.setAlignment(QtCore.Qt.AlignCenter)
        # self.spinBox_no_of_stickers.setMinimum(1)
        # self.spinBox_no_of_stickers.setMaximum(100)
        self.spinBox_no_of_stickers.setObjectName("spinBox_no_of_stickers")

        self.vl1.setAlignment(QtCore.Qt.AlignTop)
        self.vl2.setAlignment(QtCore.Qt.AlignTop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_addRecord.clicked.connect(self.addRecord)
        self.btn_removeRecord.clicked.connect(self.removeRecord)
        self.btn_okCancel.clicked.connect(self.getAllData)
        self.btn_okCancel.clicked.connect(QtWidgets.qApp.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "STICKER GENERATOR"))
        self.btn_addRecord.setText(_translate("MainWindow", "Add"))
        self.btn_removeRecord.setText(_translate("MainWindow", "Remove"))
        self.label_Attribute.setText(_translate("MainWindow", "ATTRIBUTE"))
        self.label_values.setText(_translate("MainWindow", "VALUES"))
        self.label_no_of_stickers.setText(_translate("MainWindow", "Number of Stickers"))
        # self.menuFile.setTitle(_translate("MainWindow", "File"))
        # self.menuStorage.setTitle(_translate("MainWindow", "Storage"))

    def addRecord(self):
        self.record_count += 1
        self.textinput_vl1.append(QtWidgets.QLineEdit(self.verticalLayoutWidget_2))
        self.textinput_vl2.append(QtWidgets.QLineEdit(self.verticalLayoutWidget_3))
        self.textinput_vl1[self.record_count].setObjectName("textinput_vl1" + str(self.record_count))
        self.textinput_vl2[self.record_count].setObjectName("textinput_vl2" + str(self.record_count))
        self.vl1.addWidget(self.textinput_vl1[self.record_count])
        self.vl2.addWidget(self.textinput_vl2[self.record_count])

    def removeRecord(self):
        if (self.record_count > 0):
            self.textinput_vl1[self.record_count].deleteLater()
            self.textinput_vl2[self.record_count].deleteLater()
            self.textinput_vl1.pop()
            self.textinput_vl2.pop()
            self.record_count -= 1

    def getAllData(self):
        print('Record_Count =', self.record_count + 1)
        print(self.spinBox_no_of_stickers.value())
        # for i in range(0,self.record_count+1):
        # print(self.textinput_vl1[i].text()," ",self.textinput_vl2[i].text())
        # print(self.stickers)
        self.Sticker()

    def makeimg(self, imgname, size):
        self.img = Image.new('RGB', size, "white")
        # draw = ImageDraw.Draw(img)
        self.img.save(imgname)

    def Sticker(self):
        dirname = 'Stickers_Generated'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        os.chdir(dirname)

        number = self.spinBox_no_of_stickers.value()
        self.font = ImageFont.truetype(r'./Font/times.ttf',20)
        for i in range(number):
            self.imgname = str(i + 1) + '.png'
            self.size = (700, 750)

            self.makeimg(self.imgname, self.size)
            self.image = Image.open(self.imgname)
            self.draw = ImageDraw.Draw(self.image)
            self.y = 100
            self.color = 'rgb(0, 0, 0)'  # black color
            for j in range(self.record_count):
                self.draw.text((50, self.y), self.textinput_vl1[j].text(), fill=self.color, font=self.font)
                self.draw.text((350, self.y), self.textinput_vl2[j].text(), fill=self.color, font=self.font)
                # print(self.textinput_vl1[i].text(), self.textinput_vl2[i].text())
                self.y += 40
            self.draw.text((50, self.y), self.textinput_vl1[self.record_count].text(), fill=self.color, font=self.font)
            self.draw.text((350, self.y), str(str(int(self.textinput_vl2[self.record_count].text()) + i).zfill(5)),
                           fill=self.color, font=self.font)

            str(str(i + 1).zfill(5))
            self.image.save(self.imgname)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

