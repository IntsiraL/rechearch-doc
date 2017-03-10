# -*- coding: utf-8 -*-
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from arbre import Arbre, Mot
from importdata import *


class InvertedIndex:
    """
    Construction de l'index inversé avec lemmatisation de porter

    """

    def __init__(self, _chemincorpus, *args):
        self.dictionnaire = Arbre()
        self.doc = DocParse(_chemincorpus)
        stopw = list()
        if len(args) > 0:
            stopw = StopWord(args[0])
        for d in self.doc.docList:
            for w in d.getWord(stopw):
                self.dictionnaire.majMotArbre(w)

    def __str__(self):
        print(self.dictionnaire)
        return ""

    def findDoc(self, *args):
        """

        :param args: Liste des mots dans une réquete
        :return: L
        """
        return self.dictionnaire.recupInfoMot("dd")


class Requete:
    """
    Tout ce qui gère la requête:
        -Réquête bolléenne
    """

    def __init__(self, _req):
        self.req = _req

    def querieState(self):
        porter = PorterStemmer()
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.req)
        return [porter.stem(w) for w in word_tokens if (not w in stop_words) and (not w in string.punctuation)]

    def booleanQuerie(self, _index, _type,*args):
        """
        Requete booleen AND
        :param _index: l'index inversé
        :param args: liste des mots qui forme la requete
        :param _type: AND | OR
        :return: liste des doc id trouvés par la methode d'intersection ou d'union
        """
        listM = list()
        listid = list()
        if len(args)== 0:
            # selection tous les objets mots qu'on a trouvé relatif à la requete dans une liste
            for m in self.querieState():
                _mot = _index.dictionnaire.recupInfoMot(m)
                if _mot != None:
                    listM.append(_mot)
        else:
            # selection tous les objets mots qu'on a trouvé relatif à la requete dans une liste
            for m in args:
                _mot = _index.dictionnaire.recupInfoMot(m)
                if _mot != None:
                    listM.append(_mot)
        # trier la liste par raport aux longuers des list des documents de mot
        listM.sort(key=lambda m: len(m.listDoc))
        if _type == "AND":
            #cherche l'intersection
            i = 0
            while i < len(listM[0].listDoc):
                j = 1
                while j < len(listM):
                    k = 0
                    while k < len(listM[j].listDoc):
                        if  listM[0].listDoc[i]["idDc"] == listM[j].listDoc[k]["idDc"]:
                            #passer au suivant
                            break
                        k += 1
                    if k == len(listM[j].listDoc):
                        #on a pas trouvé l'id
                        break
                    j += 1
                if j == len(listM):
                    #j'ai trouvé
                    listid.append(listM[0].listDoc[i]["idDc"])
                i += 1
        elif _type == "OR":
            for m in listM[-1].listDoc:
                listid.append(m["idDc"])
            i = 0
            while i < len(listM)-1:
                for d in listM[i].listDoc:
                    if not d["idDc"] in listid:
                        listid.append(d["idDc"])
                i += 1
        return listid

    def biwordQuerie(self,_index):
        """
        The query stanford university palo alto can be broken into the Boolean query on biwords:
        ``stanford OR university'' AND ``university OR palo'' AND ``palo OR alto''
        ``stanford AND university'' OR``university AND palo'' OR ``palo AND alto''
        :param _index:
        :return: liste des doc id trouvés
        """
        token = self.querieState()
        if len(token) > 2:
            listM = list()
            listid = list()
            i = 0
            while i < len(token) - 1:
                listM.append(self.booleanQuerie(_index, "OR", token[i], token[i + 1]))
                i += 1
            # trier la liste par raport aux longuers des list des documents de mot
            listM.sort(key=lambda m: len(m))
            # cherche l'intersection
            i = 0
            while i < len(listM[0]):
                j = 1
                while j < len(listM):
                    k = 0
                    while k < len(listM[j]):
                        if listM[0][i] == listM[j][k]:
                            # passer au suivant
                            break
                        k += 1
                    if k == len(listM[j]):
                        # on a pas trouvé l'id
                        break
                    j += 1
                if j == len(listM):
                    # j'ai trouvé
                    listid.append(listM[0][i])
                i += 1
            if listid != []:
                print("biword AND")
                return listid
            else:
                listM = []
                i = 0
                while i < len(token) - 1:
                    listM.append(self.booleanQuerie(_index, "AND", token[i], token[i + 1]))
                    i += 1
                # trier la liste par raport aux longuers des list des documents de mot
                listM.sort(key=lambda m: len(m))
                listid = listM[-1]
                i = 0
                while i < len(listM) - 1:
                    for d in listM[i]:
                        if not d in listid:
                            listid.append(d)
                    i += 1
                print("biword OR")
                return listid
        else:
            v = self.booleanQuerie(_index, "AND")
            if v != []:
                return v
            else:
                return self.booleanQuerie(_index, "OR")



