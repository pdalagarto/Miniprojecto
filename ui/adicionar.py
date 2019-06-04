# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adicionar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 246)
        MainWindow.setStyleSheet("font: 14pt \"Microsoft YaHei\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.guardar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.guardar_pushButton.setObjectName("guardar_pushButton")
        self.horizontalLayout_2.addWidget(self.guardar_pushButton)
        self.cancelar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar_pushButton.setObjectName("cancelar_pushButton")
        self.horizontalLayout_2.addWidget(self.cancelar_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nome_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nome_lineEdit.setObjectName("nome_lineEdit")
        self.verticalLayout_2.addWidget(self.nome_lineEdit)
        self.marca_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.marca_lineEdit.setObjectName("marca_lineEdit")
        self.verticalLayout_2.addWidget(self.marca_lineEdit)
        self.preco_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.preco_lineEdit.setObjectName("preco_lineEdit")
        self.verticalLayout_2.addWidget(self.preco_lineEdit)
        self.imagem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.imagem_lineEdit.setObjectName("imagem_lineEdit")
        self.verticalLayout_2.addWidget(self.imagem_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.imagem_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.imagem_pushButton.setObjectName("imagem_pushButton")
        self.verticalLayout_3.addWidget(self.imagem_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Janela de Adicionar"))
        self.guardar_pushButton.setText(_translate("MainWindow", "Guardar"))
        self.cancelar_pushButton.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Marca:"))
        self.label_3.setText(_translate("MainWindow", "Preço:"))
        self.label_4.setText(_translate("MainWindow", "Imagem:"))
        self.imagem_pushButton.setText(_translate("MainWindow", "Imagem"))
