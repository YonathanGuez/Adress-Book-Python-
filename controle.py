#!/usr/bin/python

from PyQt4.QtGui import QInputDialog, QLineEdit,QPushButton,QProgressBar,QSlider, QWidget,QApplication, QFont,QMessageBox,QTreeWidgetItem,QFileDialog
from PyQt4.QtCore import QObject, SIGNAL, SLOT, Qt, QCoreApplication,QLocale, QTranslator, QString, QLibraryInfo

import carnet,Ajoute,save, sys,Model, os

class Controlleur:
    	def __init__(self,a,Programme,FAjouter,Delete,Change,Search,Save):

		self.FAjouter=FAjouter
		self.Programme=Programme
		self.Delete=Delete
		self.Change=Change
		self.Search=Search
		self.Save=Save
		self.signaux()
		#creation du carnet dans le controleur 
		self.AC = Model.carnet()
		
	
	def signaux(self):
		#on regroupe tout les signaux de la page d affichage 
		self.Programme.fe.pushButton_3.clicked.connect(self.showAdd)
		self.Programme.fe.pushButton_4.clicked.connect(self.ChangeCont)
		self.Programme.fe.pushButton_2.clicked.connect(self.suppCont)
		self.Programme.fe.pushButton.clicked.connect(self.searchCont)
		self.Programme.fe.actionNouveau_repertoir.triggered.connect(self.SaveCSV)
		self.Programme.fe.actionSupprimer_repertoir.triggered.connect(self.SuppRep)
		self.Programme.fe.actionQuitter.triggered.connect(self.Quitter)
		#on regroupe tout les signaux de la  page d ajout d un element 
		self.FAjouter.Aj.pushButton.clicked.connect(self.ValideAdd)
		self.FAjouter.Aj.pushButton_2.clicked.connect(self.AnnulAdd)
		#on regroupe tout les signaux de la  page de suppresion d un element 
		self.Delete.delete.pushButton.clicked.connect(self.ValideDel)
		#on regroupe tout les signaux de la  page de Modification d un element
		self.Change.change.pushButton.clicked.connect(self.ValidChange)
		#on regroupe tout les signaux de la  page de Recherche d un element
		self.Search.SC.pushButton_2.clicked.connect(self.ValidSearch)
		self.Search.SC.pushButton.clicked.connect(self.closeSearch)
		#on regroupe tout les signaux de la page de sauvegarde widget 
		self.Save.save.pushButton.clicked.connect(self.ValidSave)
		self.Save.save.pushButton_2.clicked.connect(self.closeSave)
#FONCTION DE RAFRECHISEMENT DU TABLEAU 
	def RechargeEcrant(self) :
		self.Programme.fe.treeWidget.clear()
		for elt in self.AC.clients:
			QT = QTreeWidgetItem()
    			QT.setText(0, elt.getNom() )
    			QT.setText(1, elt.getPrenom() )
    			QT.setText(2, elt.getNumero() )
    		       	self.Programme.fe.treeWidget.addTopLevelItem(QT)
#AFFICHAGE DE LA NOUVELLE FENETRE AJOUTE
	def showAdd(self):
		self.FAjouter.affichage()
		
	def ValideAdd(self):
		nom = self.FAjouter.Aj.nomLineEdit.text()
		prenom = self.FAjouter.Aj.prenomLineEdit.text()
		numero = self.FAjouter.Aj.numeroLineEdit.text()
		print (nom)
		print(prenom)
		print (numero)
		contacte1 = Model.client(nom,prenom,numero)
		self.AC.ajouterClient(contacte1)
		self.RechargeEcrant()
		self.AC.affiche_client()
	
	def AnnulAdd(self):
		self.FAjouter.fermer()

	
#AFFICHER UNE NOUVELLE FENETRE DE MODIFICATION
	
	def ChangeCont(self):
		self.Change.affichage()

	def ValidChange(self):
		nom = self.Change.change.nomLineEdit.text()
		prenom = self.Change.change.prenomLineEdit.text()
		NewNom = self.Change.change.nouveauNomLineEdit.text()
		NewPre = self.Change.change.nouveauPrenomLineEdit.text()
		NewNum = self.Change.change.nouveauNumeroLineEdit.text()
		contacte1 = Model.client(NewNom,NewPre,NewNum)
		i = self.AC.recherche_Contact(nom,prenom)
		if i != -1:
			self.AC.remplacerClient(i,contacte1)
			self.RechargeEcrant()
		else:
			print " Aucun contact de se nom ou prenom "
		self.AC.affiche_client()
		self.Change.fermer()

#AFFICHER UNE NOUVELLE FENETRE DE SUPPRESSION
	def suppCont(self):
		self.Delete.affichage()

	def ValideDel(self):
		nom = self.Delete.delete.nomLineEdit.text()
		prenom = self.Delete.delete.prenomLineEdit.text()
		i = self.AC.recherche_Contact(nom,prenom)
		if i != -1:
			self.AC.Supp_contact(i)
			self.RechargeEcrant()
		else: 
			print " Aucun contact de se nom ou prenom "
		
		self.AC.affiche_client()
		self.Delete.fermer()
#AFFICHER UNE NOUVELLE FENETRE DE RECHERCHE
	def searchCont(self):
		self.Search.affichage()

	def ValidSearch(self):
		nom = self.Search.SC.rechercherNomLineEdit.text()
		prenom = self.Search.SC.rechercherPrenomLineEdit.text()
		
		self.Search.SC.treeWidget.clear()
		for elt in self.AC.clients:
			if (elt.nom == nom) or (elt.prenom == prenom):
				QT = QTreeWidgetItem()
    				QT.setText(0, elt.getNom() )
    				QT.setText(1, elt.getPrenom() )
    				QT.setText(2, elt.getNumero() )
    			       	self.Search.SC.treeWidget.addTopLevelItem(QT)
			
	def closeSearch(self):
		self.Search.fermer()

#QUITTER TOUTE LES FENETRES
	def Quitter(self):
		self.Search.fermer()
		self.FAjouter.fermer()
		self.Delete.fermer()
		self.Change.fermer()
		self.Save.fermer()
		self.Programme.fermer()

	def SuppRep(self):
		self.AC.Supp_all()
		self.RechargeEcrant()
		
#SAUVGARDER REPERTOIRE
	def SaveCSV(self):
        	self.Save.affichage()

	def ValidSave(self):
		self.AC.ExporCSV()

	def closeSave(self):
		self.Save.fermer()
		
