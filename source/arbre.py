#-*- coding: utf-8 -*-

# 1- Definition de la ClassMot : Contient un mot et ses infos

class Mot:
    """
             Attributs de la classe:
           -la chaine de caractère representant le mot : nom
            -la liste de documents q'il contient: listDoc
            - le nombre d'occurence total du mot : nbOcc
         Methodes de la classe:
            -__init__(self,name) : Constructeur avec paramètre name qui est une chaine de caractère
            -ajoutDoc(self,idDoc,occ): qui  ajout un document dans liste de documents qui le contiennent
                  -idDoc : identifiant du document
                  -occ: nombre d'occurence du mot dans le document
              -parcoursArbre(self,a): methode de test dans l'arbre qui permet d'afficher tous les mot  de l'arbre dans l'ordre
    """
            
    def __init__(self,name):
        self.nom=name
        self.listDoc=[]
        self.nbOcc=0

    def ajoutDoc(self,idDoc,occ):
        infoDoc={'idDc':idDoc,'nbOcc':occ}
        self.listDoc.append(infoDoc)
        

# 2- Creation d'un Arbre Binaire des mots du dictionnaire


class Arbre:
    """
      Attributs de la classe:
      - la racine de l'arbre : racineArbre
        - List de Noeud fils d'un Arbre ( qui est d'une liste d'Arbre): listeNoeudFils
     Methodes de la Classe:
         -__init__(self): Constucteur d'un Arbre
         -ajoutNoeudFils(self,fils): Ajout d'un Sous Arbre dans l'arbre (donc dans la liste de noeuds fils)
         -estFeuille(self): verifie si Arbre est une feuille ou contient des Noeuds fils
         -ajoutMot(self,mot): permet d'ajouter un (mot) du dictionnaire dans l'arbre
    """

    def __init__(self):
        self.listeNoeudFils=[]  
        self.racineArbre=Mot("")

    def ajoutNoeudFils(self,fils): # Ajout d'un fils dans l'arbre
        self.listeNoeudFils.append(fils)

    def estFeuille(self):
        return (self.listeNoeudFils==[])

    def ajoutMot(self,mot):
        #print("Parcours de :",self.racineArbre.nom)
        if (len(self.listeNoeudFils)==0):
            if(self.racineArbre==""):
                A=Arbre()
                A.racineArbre=mot
                self.listeNoeudFils.append(A)
            else:
                m=self.racineArbre
                B=Arbre()
                B.racineArbre=m
                A=Arbre()
                A.racineArbre=mot
                if (A.racineArbre.nom<B.racineArbre.nom):
                    self.listeNoeudFils.append(A)
                    self.listeNoeudFils.append(B)
                else:
                    self.listeNoeudFils.append(B)
                    self.listeNoeudFils.append(A)
        else:
            if (len(self.listeNoeudFils)==1):
                
                A=self.listeNoeudFils[0]
                B=Arbre()
                B.racineArbre=mot
                self.listeNoeudFils=[]
                if (A.racineArbre.nom<B.racineArbre.nom):
                    self.listeNoeudFils.append(A)
                    self.listeNoeudFils.append(B)
                else:
                    self.listeNoeudFils.append(B)
                    self.listeNoeudFils.append(A)
                    
            else:
                a=self.listeNoeudFils[1].racineArbre.nom
                if (mot.nom<a):
                    #print("Parcours de :",self.listeNoeudFils[0].racineArbre.nom)
                    self.listeNoeudFils[0].ajoutMot(mot)
                else:
                    #print("Parcours de :",self.listeNoeudFils[1].racineArbre.nom)
                    self.listeNoeudFils[1].ajoutMot(mot)

    def parcoursArbre(self):
        if (self.listeNoeudFils==[]):
            print ( "feuille :", self.racineArbre.nom)
        else:
            #print ( "noeud :", self.racineArbre.nom)
            #print ("taille neoud:",len (self.listeNoeudFils))
            for i in self.listeNoeudFils:
                i.parcoursArbre()
            #print ("------------------")
        



#brouillon: test----------------------------------------
#print (mot1.listDoc)
##mot1=Mot("hello")
##mot2=Mot("bonjour")
##mot3=Mot("bonsoir")
##mot4=Mot("zadi")
##mot4=Mot("zadi")
##mot5=Mot("a")
##mot6=Mot("bonj")
##mot7=Mot("thomas")
##A=Arbre()
#A.racineArbre=mot1
##A.ajoutMot(mot1)

#print ("nom racine ",A.racineArbre.nom)
##A.ajoutMot(mot2)
##A.ajoutMot(mot3)
##A.ajoutMot(mot4)
##A.ajoutMot(mot5)
##A.ajoutMot(mot6)
##A.ajoutMot(mot7)
##print ("------------------------")
##
##A.parcoursArbre()


##mot1.ajoutDoc(1,10)
##
##A=Arbre()
##A.ajoutNoeudFils(mot1)
##print (A.estFeuille())



#print( ""<"a")

