# -*- coding: utf-8 -*-

from nltk.stem.porter import PorterStemmer
from .arbre import Arbre,Mot

class InvertedIndex:
    """
    Construction de l'index inversé avec lemmatisation de porter

    """

    def __init__(self):
        self.dictionnair= Arbre()
