#!/usr/bin/python

from PyQt4.QtGui import QApplication
import carnet,Ajoute,delete,change,controle,search,save, sys


def main(args):
	a=QApplication(args)
    	Programme= carnet.fenPrincipale(args)
	FAjouter=Ajoute.fenPrincipale(args)
	Delete=delete.fenPrincipale(args)
	Change=change.fenPrincipale(args)
	Search=search.fenPrincipale(args)
	Save=save.fenPrincipale(args)
	controle1=controle.Controlleur(a,Programme,FAjouter,Delete,Change,Search,Save)
	Programme.show()
	r=a.exec_()
    	return r
if __name__=="__main__":
        main(sys.argv)
