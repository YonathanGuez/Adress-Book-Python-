#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import string
import pickle
import os


class client:
    def __init__(self,nom,prenom,numero):
        self.nom=nom
        self.prenom=prenom
        self.numero=numero
    
    def getNom(self):
	return self.nom

    def getPrenom(self):
	return self.prenom

    def getNumero(self):
	return self.numero
        
class carnet:
    def __init__(self):
        self.clients = []
    
    # sauver la liste de clients dans le fichier
    def sauver(self):
        f = file(self.filename,'w')
        pickle.dump(self.clients,f) 
        f.close()
        
    def ajouterClient(self, c):
        self.clients.append(c)
    
    def affiche_client(self):
		for i in self.clients:
			print (i.nom,i.prenom,i.numero)

    def remplacerClient(self,index,c):
        self.clients[index]=c
        
    def client(self,indice):
        return self.clients[indice]

    def recherche_Contact(self,recherche,recherche2):
		i = 0
		for elt in self.clients:
			if ((recherche == elt.nom) and (recherche2 == elt.prenom)):

				return i
			i = i + 1
		return -1

    def Supp_contact(self,indice):
		self.clients.pop(indice) 

    def	Supp_all(self):
		i=0
		for elt in self.clients:
			del self.clients[i]
			i=i+1
    def ExporCSV(self):
		#commende de dialogue perfaite pour enregistrer un fichier
		QtGui.QFileDialog.getSaveFileName(self,"Enregistrer carnet d adresse", '',"Carnet d adresse (*.csv)")
		pickle.dump(self.clients, out_file)
        	out_file.close()
    
