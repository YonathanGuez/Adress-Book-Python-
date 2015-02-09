#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_Ajoute import *

import Model,sys, os

class fenPrincipale(QMainWindow,Ui_fenetre2):
    	def __init__(self,args):
		QMainWindow.__init__(self,None)
		qapp = QCoreApplication.instance()
		self.Aj=Ui_fenetre2()
		self.Aj.setupUi(self)
		self.Aj.pushButton.setShortcut(QKeySequence(QtCore.Qt.Key_Return))
		self.Aj.pushButton_2.setShortcut(QKeySequence("Ctrl+A"))

	def affichage(self):
           	self.show()
	def fermer(self):
		self.close()

