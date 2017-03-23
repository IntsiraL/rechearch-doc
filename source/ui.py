from requette import Requete
import os.path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QTextEdit, \
    QScrollArea
from functools import partial


class Fen(QWidget):
    """
    Fenêtre principale
    """

    def __init__(self, _index,):
        super().__init__()
        self.index = _index
        self.textQuerie = QLineEdit()
        self.searchBt = QPushButton("Search")
        self.vbox = QVBoxLayout()

        self.setUI()
        self.setFixedSize(600, 500)
        self.searchBt.clicked.connect(self.afficheResult)

    def setUI(self):

        label = QLabel()
        chemin = os.path.abspath(os.path.split(__file__)[0])
        chemin += "/../Data/search.png"
        label.setPixmap(QPixmap(chemin))
        hbox1 = QHBoxLayout()
        hbox1.addWidget(label, 0, Qt.AlignCenter)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.textQuerie)
        hbox2.addWidget(self.searchBt)
        hbox2.setAlignment(Qt.AlignTop)

        vboxL = QVBoxLayout()
        vboxL.addLayout(hbox1)
        vboxL.addLayout(hbox2)
        vboxL.addLayout(self.vbox)

        self.setLayout(vboxL)

        # self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Recherche documentaire')

        self.show()

    def afficheResult(self):
        self.clearLayout(self.vbox)
        if self.textQuerie.text() != "":
            req = Requete(self.textQuerie.text())
            scroll = QScrollArea()
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setWidgetResizable(False)
            widget = QWidget()
            resBox = QVBoxLayout()
            for doc in req.vectorQuerie(self.index):
                if doc != None:
                    docBt = QPushButton(doc.docno)
                    resBox.addWidget(docBt)
                    docBt.clicked.connect(partial(self.aff, doc))
                    if len(doc.head) > 0:
                        for head in doc.head:
                            label1 = QLabel(head)
                            resBox.addWidget(label1)
                    else:
                        label1 = QLabel(doc.first)
                        resBox.addWidget(label1)

            widget.setLayout(resBox)
            scroll.update()
            scroll.setWidget(widget)
            self.vbox.addWidget(scroll)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())

    def aff(self, _doc):
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
        d.setFixedSize(400,600)
        d.show()
