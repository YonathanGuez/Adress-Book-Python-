#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_delete import *

import Model,sys, os

class fenPrincipale(QMainWindow,Ui_Dialog):
    	def __init__(self,args):
		QMainWindow.__init__(self,None)
		qapp = QCoreApplication.instance()
		self.delete=Ui_Dialog()
		self.delete.setupUi(self)
		self.delete.pushButton.setShortcut(QKeySequence(QtCore.Qt.Key_Return))
	def affichage(self):
           	self.show()
	
	def fermer(self):
		self.close()
