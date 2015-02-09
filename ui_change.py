# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created: Sun Oct  5 15:43:02 2014
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
        Dialog.resize(389, 309)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 40, 301, 71))
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
        self.formLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 150, 301, 111))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.nouveauNomLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.nouveauNomLabel.setObjectName(_fromUtf8("nouveauNomLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.nouveauNomLabel)
        self.nouveauNomLineEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.nouveauNomLineEdit.setObjectName(_fromUtf8("nouveauNomLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.nouveauNomLineEdit)
        self.nouveauPrenomLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.nouveauPrenomLabel.setObjectName(_fromUtf8("nouveauPrenomLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.nouveauPrenomLabel)
        self.nouveauPrenomLineEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.nouveauPrenomLineEdit.setObjectName(_fromUtf8("nouveauPrenomLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.nouveauPrenomLineEdit)
        self.nouveauNumeroLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.nouveauNumeroLabel.setObjectName(_fromUtf8("nouveauNumeroLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.nouveauNumeroLabel)
        self.nouveauNumeroLineEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.nouveauNumeroLineEdit.setObjectName(_fromUtf8("nouveauNumeroLineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.nouveauNumeroLineEdit)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 120, 171, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 241, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Modifier un Contact", None))
        self.nomLabel.setText(_translate("Dialog", "Nom", None))
        self.prenomLabel.setText(_translate("Dialog", "Prenom", None))
        self.nouveauNomLabel.setText(_translate("Dialog", "Nouveau Nom", None))
        self.nouveauPrenomLabel.setText(_translate("Dialog", "Nouveau Prenom", None))
        self.nouveauNumeroLabel.setText(_translate("Dialog", "Nouveau Numero", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.label.setText(_translate("Dialog", "Modifier votre contact:", None))
        self.label_2.setText(_translate("Dialog", "Saisir le contact a modifier :", None))

