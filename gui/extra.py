# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vertical1 = QtWidgets.QVBoxLayout()
        self.vertical1.setObjectName("vertical1")
        self.horizontalLayout.addLayout(self.vertical1)
        self.vertical2 = QtWidgets.QVBoxLayout()
        self.vertical2.setObjectName("vertical2")
        self.drinks_list = QtWidgets.QVBoxLayout()
        self.drinks_list.setObjectName("drinks_list")
        self.vertical2.addLayout(self.drinks_list)
        self.label_total_price = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_total_price.sizePolicy().hasHeightForWidth())
        self.label_total_price.setSizePolicy(sizePolicy)
        self.label_total_price.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_total_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_price.setObjectName("label_total_price")
        self.vertical2.addWidget(self.label_total_price)
        self.horizontalLayout.addLayout(self.vertical2)
        self.vertical3 = QtWidgets.QVBoxLayout()
        self.vertical3.setObjectName("vertical3")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)
        self.label_username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_username.setObjectName("label_username")
        self.vertical3.addWidget(self.label_username)
        self.button_buy = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_buy.sizePolicy().hasHeightForWidth())
        self.button_buy.setSizePolicy(sizePolicy)
        self.button_buy.setObjectName("button_buy")
        self.vertical3.addWidget(self.button_buy)
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setObjectName("button_cancel")
        self.vertical3.addWidget(self.button_cancel)
        self.button_reload = QtWidgets.QPushButton(self.centralwidget)
        self.button_reload.setObjectName("button_reload")
        self.vertical3.addWidget(self.button_reload)
        self.horizontalLayout.addLayout(self.vertical3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button_buy.clicked.connect(MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_total_price.setText(_translate("MainWindow", "Total: 0.00$"))
        self.label_username.setText(_translate("MainWindow", "--name--"))
        self.button_buy.setText(_translate("MainWindow", "buy"))
        self.button_cancel.setText(_translate("MainWindow", "cancel"))
        self.button_reload.setText(_translate("MainWindow", "reload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

