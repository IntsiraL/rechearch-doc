# -*- coding: utf-8 -*-
from xml.dom import minidom
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from arbre import Mot


class Document:
    """
    Classe Définissant un document caractérisé pae:
    -docno
    -fileid
    -first
    -second
    -head
    -dateline
    -text

    """
    nbdocuments = 0  # le nombre des documents

    def __init__(self, _docno, _fileid, _first, _second, _head, _byline, _dateline, _text):
        Document.nbdocuments += 1
        self.id = Document.nbdocuments  # identifiant pour le doc pour être sûr
        self.docno = _docno
        self.fileid = _fileid
        self.first = _first
        self.second = _second
        self.head = _head
        self.byline = _byline
        self.dateline = _dateline
        self.text = _text

    def nombreDoc(cls):
        """Methode de classe affichant combien de document ont été créé"""
        print("Jusqu'à présent, {} documents ont été crées".format(cls.nbdocuments))

    nombreDoc = classmethod(nombreDoc)

    def getWord(self, *args):
        """
        Recupère les mots d'un document
        :param args: Liste des stopwords personnel
        :return: Liste des mots de ce documents
        """
        listWord = list()
        porter = PorterStemmer()
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.text)
        qq = ["``", "''", "...", "'s"]
        if len(args) > 0:
            word = [porter.stem(w) for w in word_tokens if
                    (not w in stop_words) and (not w in string.punctuation) and (not w in qq) and (not w in args)]
        else:
            word = [porter.stem(w) for w in word_tokens if (not w in stop_words) and (not w in string.punctuation) and (not w in qq)]
        mot_exit_deja = list()
        for w in word:
            if not w in mot_exit_deja:
                i = 0
                for x in word:
                    if w == x:
                        i += 1
                mot = Mot(w)
                mot.ajoutDoc(self.id, i)
                listWord.append(mot)
                mot_exit_deja.append(w)
        return listWord

    def __str__(self):
        return "(docno: {0}, fileid: {1})".format(self.docno, self.fileid)


class DocParse:
    """Parse les documents initialement en xml"""

    def __init__(self, chemin):
        l = list()
        tree = minidom.parse(chemin)
        root = tree.documentElement
        docno = ""
        fileid = ""
        first = ""
        second = ""
        for current in root.getElementsByTagName("DOC"):
            for elemt in current.getElementsByTagName("DOCNO"):
                docno = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("FILEID"):
                fileid = elemt.firstChild.nodeValue
            text = ""
            for elemt in current.getElementsByTagName("TEXT"):
                text = text + elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("FIRST"):
                first = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("SECOND"):
                second = elemt.firstChild.nodeValue
            dateline = list()
            for elemt in current.getElementsByTagName("DATELINE"):
                dateline.append(elemt.firstChild.nodeValue)
            head = list()
            for elemt in current.getElementsByTagName("HEAD"):
                head.append(elemt.firstChild.nodeValue)

            byline = list()
            for elemt in current.getElementsByTagName("BYLINE"):
                byline.append(elemt.firstChild.nodeValue)

            doc = Document(docno, fileid, first, second, head, byline, dateline, text)
            l.append(doc)

        self.docList = l

    def getDoc(self,_id):
        """
        Checher un document à partir de son id
        Il faut quand même être sur que le id existe vraiment pour éviter une erreur
        :param _id: le id du document à chercher
        :return: Le document rechercher
        """
        i = 0
        while i < len(self.docList):
            if self.docList[i].id == _id:
                break
            i += 1
        if i != len(self.docList):
            return self.docList[i]
        else:
            return None

class StopWord:
    """
    Stocker et manipuler les stops words dans une liste
    penser à ameliorer la structure dans une version suivante

    """

    def __init__(self, chemin):
        l = list()
        # peut être à bien vérifier que le fichier est bien ouvert et pas de probleme
        fichier = open(chemin, "r")
        for ligne in fichier:
            if len(ligne) > 1:
                l.append(ligne[:(len(ligne) - 1)])
        fichier.close()
        self.listStopWord = l

    def addStopword(self, mot):
        self.listStopWord.append(mot)

    def find(self, mot):
        return mot in self.listStopWord
