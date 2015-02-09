#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_save import *

import Model,sys, os

class fenPrincipale(QMainWindow,Ui_Form):
    	def __init__(self,args):
		QMainWindow.__init__(self,None)
		qapp = QCoreApplication.instance()
		self.save=Ui_Form()
		self.save.setupUi(self)
		self.save.pushButton.setShortcut(QKeySequence(QtCore.Qt.Key_Return))
		self.save.pushButton_2.setShortcut(QKeySequence("Ctrl+A"))

	def affichage(self):
           	self.show()
	def fermer(self):
		self.close()

