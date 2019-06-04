# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow4(object):
    def setup4(self, MainWindow):
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
        self.novo_guardar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.novo_guardar_pushButton.setObjectName("novo_guardar_pushButton")
        self.horizontalLayout_2.addWidget(self.novo_guardar_pushButton)
        self.novo_cancelar_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.novo_cancelar_pushButton.setObjectName("novo_cancelar_pushButton")
        self.horizontalLayout_2.addWidget(self.novo_cancelar_pushButton)
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
        self.novo_nome_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.novo_nome_lineEdit.setObjectName("novo_nome_lineEdit")
        self.verticalLayout_2.addWidget(self.novo_nome_lineEdit)
        self.novo_marca_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.novo_marca_lineEdit.setObjectName("novo_marca_lineEdit")
        self.verticalLayout_2.addWidget(self.novo_marca_lineEdit)
        self.novo_preco_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.novo_preco_lineEdit.setObjectName("novo_preco_lineEdit")
        self.verticalLayout_2.addWidget(self.novo_preco_lineEdit)
        self.novo_imagem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.novo_imagem_lineEdit.setObjectName("novo_imagem_lineEdit")
        self.verticalLayout_2.addWidget(self.novo_imagem_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.novo_imagem_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.novo_imagem_pushButton.setObjectName("novo_imagem_pushButton")
        self.verticalLayout_3.addWidget(self.novo_imagem_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Janela de Modificação"))
        self.novo_guardar_pushButton.setText(_translate("MainWindow", "Guardar"))
        self.novo_cancelar_pushButton.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Marca:"))
        self.label_3.setText(_translate("MainWindow", "Preço:"))
        self.label_4.setText(_translate("MainWindow", "Imagem:"))
        self.novo_imagem_pushButton.setText(_translate("MainWindow", "Imagem"))



