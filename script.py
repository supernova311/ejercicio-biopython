from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os.path

filename = "/home/supernova/Desktop/biopython-notebook/notebooks/data/ls_orchid.gbk"
def summarize_contents(filename):
        lista = []
        lista = os.path.split(filename)
        records= list(SeqIO.parse(filename, "genbank"))
        cadena  = ("file: " + lista[1])
        cadena += ("path: " + lista[2])
        cadena += (num_records = %i records" % len(records))
        for seq_record in SeqIO.parse(filename, "genbank"):
                cadena += ("Name: ", seq_record.name)
                cadena += ("ID: ", seq_record.id)
                cadena += (Description: ", + str (seq_record.descrition))
              print(cadena)

  summarize_contents(filename)
