#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_search import *

import Model,sys, os

class fenPrincipale(QMainWindow,Ui_Form):
    	def __init__(self,args):
		QMainWindow.__init__(self,None)
		qapp = QCoreApplication.instance()
		self.SC=Ui_Form()
		self.SC.setupUi(self)
		self.SC.pushButton_2.setShortcut(QKeySequence(QtCore.Qt.Key_Return))
		self.SC.pushButton.setShortcut(QKeySequence("Ctrl+F"))

	def affichage(self):
           	self.show()
	def fermer(self):
		self.close()

