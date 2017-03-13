# -*- coding: utf-8 -*-
from arbre import Arbre, Mot
from importdata import *
from math import log10

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

    def getListDoc(self,lisd_id):
        """
        Renvoie la liste des documents
        :param lisd_id: liste des id des documents à récuperer
        :return: La liste des documents
        """
        l = list()
        for i in lisd_id:
            l.append(self.doc.getDoc(i))
        return l

    def __str__(self):
        print(self.dictionnaire)
        return ""

    def tf_idfWeight(self,_term,_doc,_N):
        """
        Calcul le tf-idf
        :param _term: Le terme
        :param _doc: id de document
        :param _N: le nombre total des documents
        :return: Le poid du terme
        """
        m = self.dictionnaire.recupInfoMot(_term)
        #calcul de log term frequency
        tf = 0
        idf = 0
        i = 0
        if m != None:
            while i < len(m.listDoc):
                if _doc == m.listDoc[i]["idDc"]:
                    tf = 1 + log10(m.listDoc[i]["nbOcc"])
                    break
                i += 1
            # calcul le idf
            idf = log10(_N / len(m.listDoc))
        return tf*idf








