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

    def __init__(self, name):
        """

        :param name:
        """
        self.nom = name
        self.listDoc = []
        self.nbOcc = 0

    def ajoutDoc(self, idDoc, occ):
        infoDoc = {'idDc': idDoc,'nbOcc': occ}
        self.listDoc.append(infoDoc)

    def __str__(self):
        return "[nom:{0}, nbOcc:{1}, listDoc:{2}]".format(self.nom, self.nbOcc, self.listDoc)

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
         -estDansArbre(self,mot): verifie si un mot est dans l'arbre
         -majMotArbre(self,mot): permet de mettre à jour d'indexation du mot dans l'arbre
                  -Ajout le mot dans l'arbre s'il n'y est pas encore ou sinon on le met à jour
    """

    def __init__(self):
        self.listeNoeudFils = []
        self.racineArbre = Mot("")

    def ajoutNoeudFils(self, fils): # Ajout d'un fils dans l'arbre
        self.listeNoeudFils.append(fils)

    def estFeuille(self):
        return (self.listeNoeudFils == [])

    def ajoutMot(self, mot):
        #print("Parcours de :",self.racineArbre.nom)
        if (len(self.listeNoeudFils) == 0):
            if(self.racineArbre == ""):
                A = Arbre()
                A.racineArbre = mot
                self.listeNoeudFils.append(A)
            else:
                m = self.racineArbre
                B = Arbre()
                B.racineArbre = m
                A = Arbre()
                A.racineArbre = mot
                if (A.racineArbre.nom < B.racineArbre.nom):
                    self.listeNoeudFils.append(A)
                    self.listeNoeudFils.append(B)
                else:
                    self.listeNoeudFils.append(B)
                    self.listeNoeudFils.append(A)
        else:
            if (len(self.listeNoeudFils) == 1):
                
                A = self.listeNoeudFils[0]
                B = Arbre()
                B.racineArbre = mot
                self.listeNoeudFils = []
                if (A.racineArbre.nom < B.racineArbre.nom):
                    self.listeNoeudFils.append(A)
                    self.listeNoeudFils.append(B)
                else:
                    self.listeNoeudFils.append(B)
                    self.listeNoeudFils.append(A)
                    
            else:
                a = self.listeNoeudFils[1].racineArbre.nom
                if (mot.nom<a):
                    #print("Parcours de :",self.listeNoeudFils[0].racineArbre.nom)
                    self.listeNoeudFils[0].ajoutMot(mot)
                else:
                    #print("Parcours de :",self.listeNoeudFils[1].racineArbre.nom)
                    self.listeNoeudFils[1].ajoutMot(mot)

    def parcoursArbre(self):
        if (self.listeNoeudFils == []):
            print ( "feuille :", self.racineArbre)
        else:
            #print ( "noeud :", self.racineArbre.nom)
            #print ("taille neoud:",len (self.listeNoeudFils))
            for i in self.listeNoeudFils:
                i.parcoursArbre()
            print ("------------------")

    def estDansArbre(self, mot):
        res = False
        n = len((self.listeNoeudFils))
        #print("nombre de fils :",n)
        if (n == 0):
            #print("visite de :",self.racineArbre.nom)
            if (mot.nom == self.racineArbre.nom):
                res = True
        else:
              if (n == 1):
                  res = self.listeNoeudFils[0].estDansArbre(mot)
              else:
                  if(mot.nom >= self.listeNoeudFils[1].racineArbre.nom):
                      res = self.listeNoeudFils[1].estDansArbre(mot)
                  else:
                      res = self.listeNoeudFils[0].estDansArbre(mot)
        return res
    
    def majMotArbre(self, mot):
        if self.estDansArbre(mot) == False:
            self.ajoutMot(mot)
        else:
            n = len((self.listeNoeudFils))
            if( n == 0):
                if (mot.nom == self.racineArbre.nom):
                    self.racineArbre.listDoc.append(mot.listDoc[0])
                    self.racineArbre.nbOcc = self.racineArbre.nbOcc + mot.listDoc[0]['nbOcc']
            else:
                if ( n == 1 ):
                     self.listeNoeudFils[0].majMotArbre(mot)
                else:
                    if(mot.nom >= self.listeNoeudFils[1].racineArbre.nom):
                        self.listeNoeudFils[1].majMotArbre(mot)
                    else:
                        self.listeNoeudFils[0].majMotArbre(mot)
                        
                    
    def __str__(self):
        print("Affichage de l'arbre")
        self.parcoursArbre()
        return "Fin Parcours"
                    
            
            
        
        
            



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
##mot1_2=Mot("hello")
##A=Arbre()
###A.racineArbre=mot1
##A.majMotArbre(mot1)
##
###print ("nom racine ",A.racineArbre.nom)
##A.majMotArbre(mot2)
##        
##A.majMotArbre(mot3)
##A.majMotArbre(mot4)
##A.majMotArbre(mot5)
##A.majMotArbre(mot6)
##A.majMotArbre(mot7)
###A.majMotArbre(mot1)
###A.majMotArbre(mot1_2)
####print ("------------------------")
####
##A.parcoursArbre()
##
##print(A.estDansArbre(mot1_2))

##mot1.ajoutDoc(1,10)
##
##A=Arbre()
##A.ajoutNoeudFils(mot1)
##print (A.estFeuille())



#print( ""<"a")

