# -*- coding: utf-8 -*-

from arbre import Arbre, Mot
from importdata import *

class InvertedIndex:
    """
    Construction de l'index inversé avec lemmatisation de porter

    """

    def __init__(self, _chemincorpus, *args):
        self.dictionnaire = Arbre()
        doc = DocParse(_chemincorpus)
        stopw = list()
        if len(args) > 0:
            stopw = StopWord(args[0])
        for d in doc.docList:
            for w in d.getWord(stopw):
                self.dictionnaire.majMotArbre(w)

    def __str__(self):
        print(self.dictionnaire)
        return ""