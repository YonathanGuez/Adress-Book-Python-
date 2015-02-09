# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ajoute.ui'
#
# Created: Wed Oct  1 19:53:22 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fenetre2(object):
    def setupUi(self, fenetre2):
        fenetre2.setObjectName(_fromUtf8("fenetre2"))
        fenetre2.resize(413, 324)
        fenetre2.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(fenetre2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.nomLabel = QtGui.QLabel(self.formLayoutWidget)
        self.nomLabel.setObjectName(_fromUtf8("nomLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nomLabel)
        self.nomLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.nomLineEdit.setObjectName(_fromUtf8("nomLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nomLineEdit)
        self.prenomLabel = QtGui.QLabel(self.formLayoutWidget)
        self.prenomLabel.setObjectName(_fromUtf8("prenomLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.prenomLabel)
        self.prenomLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.prenomLineEdit.setObjectName(_fromUtf8("prenomLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.prenomLineEdit)
        self.numeroLabel = QtGui.QLabel(self.formLayoutWidget)
        self.numeroLabel.setObjectName(_fromUtf8("numeroLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.numeroLabel)
        self.numeroLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.numeroLineEdit.setObjectName(_fromUtf8("numeroLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numeroLineEdit)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 140, 241, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        fenetre2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fenetre2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fenetre2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fenetre2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fenetre2.setStatusBar(self.statusbar)

        self.retranslateUi(fenetre2)
        QtCore.QMetaObject.connectSlotsByName(fenetre2)

    def retranslateUi(self, fenetre2):
        fenetre2.setWindowTitle(_translate("fenetre2", "Ajouter un Contact", None))
        fenetre2.setToolTip(_translate("fenetre2", "<html><head/><body><p><br/></p></body></html>", None))
        fenetre2.setWhatsThis(_translate("fenetre2", "<html><head/><body><p><br/></p></body></html>", None))
        self.nomLabel.setText(_translate("fenetre2", "Nom", None))
        self.prenomLabel.setText(_translate("fenetre2", "Prenom", None))
        self.numeroLabel.setText(_translate("fenetre2", "Numero", None))
        self.pushButton.setText(_translate("fenetre2", "OK", None))
        self.pushButton_2.setText(_translate("fenetre2", "Annuler", None))

