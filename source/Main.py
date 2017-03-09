# -*- coding: utf-8 -*-

import argparse
import os.path
from importdata import *

parser = argparse.ArgumentParser()
parser.add_argument("d",type = str ,help="Le chemin de la document")
parser.add_argument("s",type = str ,help="Le chemin du fichier contenant les stopwords")
args = parser.parse_args()

if os.path.isfile(args.d) and os.path.isfile(args.s):
    doc = DocParse(args.d)
    doc.docList[0].nombreDoc()
    print("Premier doc {}".format(doc.docList[1]))
    print(doc.docList[0].getWord()[0].listDoc)
    stopw = StopWord(args.s)
    t = "about"
    if stopw.find(t):
        print("Yes")
    else:
        print("No")
    print("Premier stopword {}".format(stopw.listStopWord[1]))

    print("Fin")
else:
    print("ERROR: le(s) document(s) que vous avez indiqué n'existe pas")
