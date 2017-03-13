from requette import Requete
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QTextEdit
from functools import partial

class Fen(QWidget):
    """
    Fenêtre principale
    """

    def __init__(self,_index):
        super().__init__()
        self.index = _index
        self.textQuerie = QLineEdit()
        self.searchBt = QPushButton("Search")
        self.vbox = QVBoxLayout()
        self.setUI()
        self.searchBt.clicked.connect(self.afficheResult)

    def setUI(self):

        label = QLabel("SEARCH ENGINE")

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.textQuerie)
        hbox2.addWidget(self.searchBt)

        vboxL = QVBoxLayout()
        vboxL.addLayout(hbox1)
        vboxL.addLayout(hbox2)
        vboxL.addLayout(self.vbox)

        self.setLayout(vboxL)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Recherche documentaire')

        self.show()

    def afficheResult(self):
        self.clearLayout(self.vbox)
        if self.textQuerie.text() != "":
            req = Requete(self.textQuerie.text())
            for doc in req.vectorQuerie(self.index):
                if doc != None:
                    resBox = QVBoxLayout()
                    docBt = QPushButton(doc.docno)
                    resBox.addWidget(docBt)
                    docBt.clicked.connect(partial(self.aff, doc))
                    for head in doc.head:
                        label1 = QLabel(head)
                        resBox.addWidget(label1)
                    self.vbox.addLayout(resBox)

    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())

    def aff(self,_doc):
        """
        Affiche document finale
        :param _doc: Object Document
        :return:
        """
        d = QDialog(self)
        vbox = QVBoxLayout()
        text = QTextEdit(_doc.text)
        vbox.addWidget(text)
        d.setLayout(vbox)
        d.setWindowTitle(_doc.docno)
        d.show()
