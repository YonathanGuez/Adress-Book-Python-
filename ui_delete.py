# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created: Sun Oct  5 14:46:20 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 183)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 341, 71))
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
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Supprimer un Contact", None))
        self.nomLabel.setText(_translate("Dialog", "Nom", None))
        self.prenomLabel.setText(_translate("Dialog", "Prenom", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))

