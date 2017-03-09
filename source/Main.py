import argparse
import os.path
from importdata import DocParse,Document

parser = argparse.ArgumentParser()
parser.add_argument("d",type = str ,help="Le chemin de la document")
args = parser.parse_args()

if os.path.isfile(args.d):
    doc = DocParse(args.d)
    doc.docList[0].nombreDoc()
    print("Premier doc {}".format(doc.docList[1]))
    print("Fin")
else:
    print("ERROR: le document que vous avez indiqué n'existe pas")
