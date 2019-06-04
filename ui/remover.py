# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remover.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow3(object):
    def setup3(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 187)
        MainWindow.setStyleSheet("font: 14pt \"Microsoft YaHei\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.horizontalLayout.addWidget(self.id_lineEdit)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.remv_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.remv_pushButton.setObjectName("remv_pushButton")
        self.horizontalLayout_2.addWidget(self.remv_pushButton)
        self.cncl_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cncl_pushButton.setObjectName("cncl_pushButton")
        self.horizontalLayout_2.addWidget(self.cncl_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.remv_pushButton.setText(_translate("MainWindow", "Remover"))
        self.cncl_pushButton.setText(_translate("MainWindow", "Cancelar"))



