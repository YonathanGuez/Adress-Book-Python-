# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created: Tue Oct  7 01:42:23 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(450, 301)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 16, 431, 271))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.rechercherNomLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.rechercherNomLabel.setObjectName(_fromUtf8("rechercherNomLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.rechercherNomLabel)
        self.rechercherNomLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.rechercherNomLineEdit.setObjectName(_fromUtf8("rechercherNomLineEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.rechercherNomLineEdit)
        self.rechercherPrenomLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.rechercherPrenomLabel.setObjectName(_fromUtf8("rechercherPrenomLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.rechercherPrenomLabel)
        self.rechercherPrenomLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.rechercherPrenomLineEdit.setObjectName(_fromUtf8("rechercherPrenomLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.rechercherPrenomLineEdit)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.treeWidget = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Rechercher", None))
        self.rechercherNomLabel.setText(_translate("Form", "Rechercher Nom:", None))
        self.rechercherPrenomLabel.setText(_translate("Form", "Rechercher Prenom:", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Nom", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Prenom", None))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Numero", None))
        self.pushButton_2.setText(_translate("Form", "Rechercher", None))
        self.pushButton.setText(_translate("Form", "Fermer", None))

