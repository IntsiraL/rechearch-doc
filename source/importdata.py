# -*- coding: utf-8 -*-
from xml.dom import minidom

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
    nbdocuments = 0 #le nombre des documents


    def __init__(self,_docno,_fileid,_first,_second,_head,_byline,_dateline,_text):
        Document.nbdocuments += 1
        self.id = Document.nbdocuments #identifiant pour le doc pour être
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


    def __str__(self):
        return "(docno: {0}, fileid: {1})".format(self.docno,self.fileid)


class DocParse:
    """Parse les documents initialement en xml"""

    def __init__(self, chemin):
        l = list()
        tree = minidom.parse(chemin)
        root = tree.documentElement
        for current in root.getElementsByTagName("DOC"):
            for elemt in current.getElementsByTagName("DOCNO"):
                docno = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("FILEID"):
                fileid = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("TEXT"):
                text = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("FIRST"):
                first = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("SECOND"):
                second = elemt.firstChild.nodeValue
            for elemt in current.getElementsByTagName("DATELINE"):
                dateline = elemt.firstChild.nodeValue
            head =list()
            for elemt in current.getElementsByTagName("HEAD"):
                head.append(elemt.firstChild.nodeValue)

            byline = list()
            for elemt in current.getElementsByTagName("BYLINE"):
                byline.append(elemt.firstChild.nodeValue)

            doc= Document(docno,fileid,first,second,head,byline,dateline,text)
            l.append(doc)

        self.docList = l
