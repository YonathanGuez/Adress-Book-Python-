# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carnet.ui'
#
# Created: Tue Oct  7 02:17:38 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(609, 369)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeWidget = QtGui.QTreeWidget(self.centralWidget)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 609, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFichier = QtGui.QMenu(self.menuBar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionNouveau_repertoir = QtGui.QAction(MainWindow)
        self.actionNouveau_repertoir.setObjectName(_fromUtf8("actionNouveau_repertoir"))
        self.actionSupprimer_repertoir = QtGui.QAction(MainWindow)
        self.actionSupprimer_repertoir.setObjectName(_fromUtf8("actionSupprimer_repertoir"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionSauvegarder_en_CSV = QtGui.QAction(MainWindow)
        self.actionSauvegarder_en_CSV.setObjectName(_fromUtf8("actionSauvegarder_en_CSV"))
        self.menuFichier.addAction(self.actionSupprimer_repertoir)
        self.menuFichier.addAction(self.actionSauvegarder_en_CSV)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuBar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_3.setText(_translate("MainWindow", "Ajouter ", None))
        self.pushButton_4.setText(_translate("MainWindow", "Modifier", None))
        self.pushButton.setText(_translate("MainWindow", "Rechercher", None))
        self.pushButton_2.setText(_translate("MainWindow", "Supprimer", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Nom", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Prenom", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Numero", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.actionNouveau_repertoir.setText(_translate("MainWindow", "Nouveau Repertoire", None))
        self.actionSupprimer_repertoir.setText(_translate("MainWindow", "Supprimer Repertoire", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.actionSauvegarder_en_CSV.setText(_translate("MainWindow", "Sauvegarder en CSV", None))

