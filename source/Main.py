# -*- coding: utf-8 -*-

import argparse
import os.path
from index import InvertedIndex

parser = argparse.ArgumentParser()
parser.add_argument("d",type = str ,help="Le chemin de la document")
parser.add_argument("s",type = str ,help="Le chemin du fichier contenant les stopwords")
args = parser.parse_args()

if os.path.isfile(args.d) and os.path.isfile(args.s):
   index = InvertedIndex(args.d, args.s)
   print(index)
else:
    print("ERROR: le(s) document(s) que vous avez indiqué n'existe pas")
