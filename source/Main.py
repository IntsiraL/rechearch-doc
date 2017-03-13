# -*- coding: utf-8 -*-
import sys
import argparse
import os.path
from index import InvertedIndex
from ui import Fen
from PyQt5.QtWidgets import QApplication

parser = argparse.ArgumentParser()
parser.add_argument("d",type = str ,help="Le chemin de la document")
parser.add_argument("s",type = str ,help="Le chemin du fichier contenant les stopwords")
args = parser.parse_args()

if os.path.isfile(args.d) and os.path.isfile(args.s):
   print("Indexation de corpus: \n  Wait ...!!")
   index = InvertedIndex(args.d, args.s)
   monApp = QApplication(sys.argv)
   fenetre = Fen(index)
   sys.exit(monApp.exec_())

else:
    print("ERROR: le(s) document(s) que vous avez indiqué n'existe pas")
