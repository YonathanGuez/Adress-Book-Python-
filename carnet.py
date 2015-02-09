#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_carnet import *

import Model,sys, os

class fenPrincipale(QMainWindow,Ui_MainWindow):

    	def __init__(self,args):
		QMainWindow.__init__(self,None)
        	# création de la fenêtre principale
        	self.fe=Ui_MainWindow()
		self.fe.setupUi(self)
		self.fe.actionQuitter.setShortcut(QKeySequence("Ctrl+Q"))
		self.fe.actionNouveau_repertoir.setShortcut(QKeySequence("Ctrl+N"))
		self.fe.actionSauvegarder_en_CSV.setShortcut(QKeySequence("Ctrl+E"))
		self.fe.pushButton_3.setShortcut(QKeySequence("Ctrl+A"))
		self.fe.pushButton_4.setShortcut(QKeySequence("Ctrl+M"))
		self.fe.pushButton_2.setShortcut(QKeySequence("Ctrl+S"))
		self.fe.pushButton.setShortcut(QKeySequence("Ctrl+R"))

	def affichage(self):
            	self.show()

	def fermer(self):
		self.close()

